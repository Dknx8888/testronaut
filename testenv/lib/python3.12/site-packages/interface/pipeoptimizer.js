import pkg from "terminal-kit";
const { terminal } = pkg;
import { exec } from 'child_process';

export function question(path) {
	terminal( 'Please select an option [ (A)nalyze | (F)ix ]\n' ) ;
	
	terminal.yesOrNo( { yes: [ 'a' ] , no: [ 'f' ] } , function( error , result ) {
		if ( result ) {
            exec(`python -m cli analyze ${path}`, (error, stdout, stderr) => {
                console.log("Analyzing...")
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
                    console.log(stdout);
                    resolve()
                }).then(process.exit(0))
            });
		}
		else {
            exec(`python -m cli fix ${path} -y`, (error, stdout, stderr) => {
                console.log("Analyzing and Fixing...")
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
                    console.log(stdout);
                    resolve()
                }).then(process.exit(0))
            });
		}
	} ) ;
}