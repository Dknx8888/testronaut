#!/usr/bin/env node

import chalk from "chalk";
import inquirer from "inquirer";
import gradient from "gradient-string";
import chalkAnimation from "chalk-animation";
import figlet from "figlet";
import { createSpinner } from "nanospinner";
import { finalDisplay } from "./analyzeOutput.js";
import pkg from "terminal-kit";
const { terminal } = pkg;
import ora from 'ora';


let RIZZ_ART = `
  ______          __                               __
 /_  __/__  _____/ /__________  ____  ____ ___  __/ /_
  / / / _ \\/ ___/ __/ ___/ __ \\/ __ \\/ __ \`/ / / / __/
 / / /  __(__  ) /_/ /  / /_/ / / / / /_/ / /_/ / /_
/_/  \\___/____/\\__/_/   \\____/_/ /_/\\__,_/\\__,_/\\__/ 
`;

const sleep_rainbow = (ms = 2000) => new Promise((r) => setTimeout(r, ms));

// Define functions for each option
function buildTestCases() {
    console.table(["apples", "oranges", "bananas"])
}

function codePerformance() {
  console.log('\n\n')
  const spinner = ora('Analyzing code performance...\n').start();

  finalDisplay()
    .then(() => {
      console.log('\n')
      spinner.succeed('Analysis complete!');
    })
    .catch(err => {
      spinner.fail(`\nAnalysis failed: ${err.message}`);
    });
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

    terminal.green('-------------------------------------------------------\n')
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
        'Display Code Performance',
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
                    codePerformance();
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