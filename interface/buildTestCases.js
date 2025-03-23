import { exec } from 'child_process';
import terminalKit from 'terminal-kit';

const terminal = terminalKit.terminal;

export function buildTestCasesPy(flag, path) {
  // Return a new Promise
  return new Promise((resolve, reject) => {
    exec(`python3 test_gen.py ${flag} ${path}`, (error, stdout, stderr) => {
      if (error) {
        reject(error);
      } else {
        // do something with stdout if you need
        resolve(stdout.trim());
      }
    });
  });
}
