import pkg from "terminal-kit";
const { terminal } = pkg;
import { exec } from 'child_process';

export function question() {
	terminal( 'Please select an option [ (A)nalyze | (F)ix ]\n' ) ;
	
	terminal.yesOrNo( { yes: [ 'a' ] , no: [ 'f' ] } , function( error , result ) {
		if ( result ) {
            exec("python -m cli analyze samples/appspec.yml", (error, stdout, stderr) => {
                new Promise((resolve, reject) => {
                    if (error) {
                        console.error(`Error: ${error.message}`);
                        reject()
                        return;
                    }
                    if (stderr) {
                        console.error(`stderr: ${stderr}`);
                        reject()
                        return;
                    }
                    console.log(`stdout: ${stdout}`);
                    resolve()
                }).then(process.exit(0))
            });
		}
		else {
            exec("python -m cli fix samples/appspec.yml -y", (error, stdout, stderr) => {
                new Promise((resolve, reject) => {
                    if (error) {
                        console.error(`Error: ${error.message}`);
                        reject()
                        return;
                    }
                    if (stderr) {
                        console.error(`stderr: ${stderr}`);
                        reject()
                        return;
                    }
                    console.log(`stdout: ${stdout}`);
                    resolve()
                }).then(process.exit(0))
            });
		}
	} ) ;
}