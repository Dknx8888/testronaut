import {exec} from 'child_process';

export function displayAnalyze() {
    exec('python3 analyzer.py', (error, stdout, stderr) =>
    {
        if (error) {
            console.error(`Error: ${error.message}`);
            return;
          }
          if (stderr) {
            console.error(`Stderr: ${stderr}`);
            return;
          }
          let metrics = stdout.trim();
    });

    
}

displayAnalyze();