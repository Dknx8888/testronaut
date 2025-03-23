#!/usr/bin/env node

import chalk from "chalk";
import inquirer from "inquirer";
import gradient from "gradient-string";
import chalkAnimation from "chalk-animation";
import figlet from "figlet";
import { createSpinner } from "nanospinner";
import pkg from "terminal-kit";
const { terminal } = pkg;

let RIZZ_ART = `
    ____  _         ______            __    
   / __ \\(_)_______/_  __/___  ____  / /____
  / /_/ / /_  /_  / / / / __ \\/ __ \\/ / ___/
 / _, _/ / / /_/ /_/ / / /_/ / /_/ / (__  ) 
/_/ |_/_/ /___/___/_/  \\____/\\____/_/____/
`;

const sleep_rainbow = (ms = 2000) => new Promise((r) => setTimeout(r, ms));
const sleep_slow = (ms = 8000) => new Promise((r) => setTimeout(r, ms));

// Define functions for each option
function buildTestCases() {
    console.table(["apples", "oranges", "bananas"])
    // ... additional logic for option one ...
}

function codeReview() {
    terminal.green("\nFunction Two executed!\n");
    // ... additional logic for option two ...
}

function createDocumentation() {
    terminal.blue("\nl\n");
}

function refactorCode() {
    terminal.yellow("\nExiting program...\n");
    process.exit();
}


async function welcome() {
    const rainbowTitle = chalkAnimation.rainbow(RIZZ_ART);
    rainbowTitle.render();

    await sleep_rainbow();
    rainbowTitle.stop();

    terminal.green('---------------------------------------------\n')
    terminal.slowTyping(
        `Rizz your code up with our tools!`,
        {
            flashStyle: terminal.brightWhite,
            delay: 50
        },
        function() {displayMenu();}
    );
}

function displayMenu() {
    terminal.cyan('\n\nChoose an option:');

    let options = [
        'Build Test Cases',
        'Code Review',
        'Create Documentation',
        'Refactor Code'
    ]

    terminal.grabInput({mouse : 'button'});

    terminal.gridMenu(options, 
        {
            width: 80,
            itemMaxWidth: 40
        },
        function(error, response) {
            switch (response.selectedIndex) {
                case 0:
                    buildTestCases();
                    break;
                case 1:
                    codeReview();
                    break;
                case 2:
                    createDocumentation();
                    break;
                case 3:
                    refactorCode();
                    break;
                default:
                    terminal.red("\nInvalid\n");
            }
            terminal.grabInput(false);
    });
}



await welcome();