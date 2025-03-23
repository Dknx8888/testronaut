import { exec } from 'child_process';
import terminalKit from 'terminal-kit';

const terminal = terminalKit.terminal;

export function code_review(path) {
  return new Promise((resolve, reject) => {
    exec(`python3 -m code_review ${path}`, (error, stdout, stderr) => {
      if (error) {
        reject(error);
      } else {
        resolve(stdout.trim());
      }
    });
  });
}
