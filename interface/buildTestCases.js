import { exec } from 'child_process';
import { resolve } from 'path';
import terminalKit from 'terminal-kit';

const terminal = terminalKit.terminal;

function ask() {
    return new Promise((resolve, reject) => {
        terminal.cyan('\n\nChoose an option:');
        terminal.grabInput({ mouse: 'button' });
    
        let flag = true;
    
        let options = [
            'Yes',
            'No'
        ];
    
        terminal.singleColumnMenu(options,
          function (error, response) {
            switch (response.selectedIndex) {
              case 0:
                flag = true;
                break;
              case 1:
                flag = false;
                break;
              default:
                terminal.red("\nInvalid\n");
            }
            terminal.grabInput(false);
            }
        );
        resolve(flag);
    }) 

}


export function buildTestCasesPy(path) {
    return ask().then(flag => {
      return new Promise((resolve, reject) => {
        exec(`python3 test_gen.py ${flag} ${path}`, (error, stdout, stderr) => {
          if (error) {
            console.error('Error running python script:', error);
            return reject(error);
          }
          resolve(stdout.trim());
        });
      });
    });
  }