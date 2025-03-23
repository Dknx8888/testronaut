import { exec } from 'child_process';
import terminalKit from 'terminal-kit';

const term = terminalKit.terminal;

function analyzeOutput(callback) {
  exec('python3 analyzer.py', (error, stdout, stderr) => {
    if (error) {
      console.error('Error running python script:', error);
      return;
    }
    callback(stdout.trim());
  });
}

function colorComplexity(complexityString) {
  const c = complexityString.toLowerCase();

  if (c.includes('(1)') || c.includes('log')) {
    return '^G';
  }
  else if (c.includes('(n)') || c.includes('n log')) {
    return '^Y';
  }
  else {
    return '^R';
  }
}

function displayMetrics(metrics) {
  const lines = metrics.split('\n').map(line => line.trim()).filter(Boolean);

  let currentClass = '';
  let firstFunctionOfCurrentClass = false;

  const tableCells = [
    ['Class', 'Function', 'Time Complexity', 'Space Complexity']
  ];

  for (const line of lines) {
    if (line.startsWith('Class ')) {
      currentClass = line.replace('Class ', '').replace(':', '').trim();
      firstFunctionOfCurrentClass = true;
      continue;
    }

    const parts = line.split(' - ');
    if (parts.length === 3) {
      const funcName = parts[0].trim();

      const timePart = parts[1].split(':')[1].trim();
      const spacePart = parts[2].split(':')[1].trim();

      const timeColor = colorComplexity(timePart);
      const spaceColor = colorComplexity(spacePart);

      const coloredTime = `${timeColor}${timePart}^:`;
      const coloredSpace = `${spaceColor}${spacePart}^:`;

      const printedClass = firstFunctionOfCurrentClass ? currentClass : '';
      firstFunctionOfCurrentClass = false;

      tableCells.push([
        printedClass,
        funcName,
        coloredTime,
        coloredSpace
      ]);
    }
  }

  term.table(tableCells, {
    contentHasMarkup: true,

    hasBorder: true,
    borderChars: 'lightRounded',
    borderAttr: { color: 'cyan' },
    textAttr: { bgColor: 'default' },
    firstRowTextAttr: { bgColor: 'cyan' } ,

    width: 100,

    fit: true
  });
}

export function finalDisplay() {
  return new Promise((resolve, reject) => {
    analyzeOutput((result) => {
      try {
        displayMetrics(result);
        resolve();
      } catch (err) {
        reject(err);
      }
    });
  });
}

