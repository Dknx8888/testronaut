#!/usr/bin/env node

import chalk from "chalk";
import inquirer from "inquirer";
import gradient from "gradient-string";
import chalkAnimation from "chalk-animation";
import figlet from "figlet";
import { createSpinner } from "nanospinner";
import { finalDisplay } from "./analyzeOutput.js";
import { buildTestCasesPy } from "./buildTestCases.js";
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
function buildTestCases(path) {
    console.log('\n\n')
    const spinner = ora('Building test cases...\n').start();
  
    buildTestCasesPy(path)
      .then(() => {
        console.log('\n')
        spinner.succeed('Analysis complete!');
      })
      .catch(err => {
        spinner.fail(`\nAnalysis failed: ${err.message}`);
      });
}

function codePerformance(path) {
  console.log('\n\n')
  const spinner = ora('Analyzing code performance...\n').start();

  finalDisplay(path)
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
        function() {
            
            displayMenu();}
    );
}

function displayMenu() {
    terminal.cyan("\n\nPlease input the path: ")
    terminal.inputField(
      {
        echo: true,
        prompt: 'Please input the path: '
      },
      function (error, input) {
        if (error) {
          terminal.red("\nError reading input\n");
          return;
        }
  
        let path = input;

        if (path.trim() === "") {
            path = process.cwd()
        };

        terminal.red(`The chosen path: ${path}`);
  
        terminal.cyan('\n\nChoose an option:');
        terminal.grabInput({ mouse: 'button' });
  
        let options = [
            'Build Test Cases',
            'Display Code Performance',
            'Create Documentation',
            'Refactor Code'
        ];
  
        terminal.gridMenu(
          options,
          {
            width: 80,
            itemMaxWidth: 40
          },
          function (error, response) {
            switch (response.selectedIndex) {
              case 0:
                buildTestCases(path);
                break;
              case 1:
                codePerformance(path);
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
          }
        );
      }
    );
  }
  

await welcome();