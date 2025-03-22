# menu.py
import click

RIZZ_ART = r"""
    ____  _         ______            __    
   / __ \(_)_______/_  __/___  ____  / /____
  / /_/ / /_  /_  / / / / __ \/ __ \/ / ___/
 / _, _/ / / /_/ /_/ / / /_/ / /_/ / (__  ) 
/_/ |_/_/ /___/___/_/  \____/\____/_/____/  

"""

def build_test_cases():
    pass

def code_review():
    pass

def create_documentation():
    pass

def refactor_code():
    pass

@click.command()
def center_print(text: str):
    """
    Prints the given text centered in the current terminal width.
    """
    # Get terminal width (columns)
    width = click.get_terminal_size()[0]
    # Calculate how many spaces we need to indent
    # so that 'text' appears roughly in the center.
    padding = max((width - len(text)) // 2, 0)
    # Print the spaces + text
    click.echo(" " * padding + text)

@click.command()
def menu():
    """
    A demo CLI that prints ASCII art for RizzTools, shows a description, 
    and presents a 6-item menu using Click prompts.
    """
    click.clear()
    
    # Print the ASCII art
    center_print(RIZZ_ART)
    
    # Print the description under the box art
    click.echo("RizzTools: Rizz your code up with our tools!")
    click.echo("-----------------------------------------------------\n")
    
    # Present the menu
    click.echo("Select an option from the menu below:")
    click.echo("[1] Build Test Cases")
    click.echo("[2] Code Review")
    click.echo("[3] Create Documentation")
    click.echo("[4] Refactor code")
    click.echo("[5] Exit\n")
    
    # Prompt user for a choice
    choice = click.prompt("Enter your choice (1-5)", type=int)
    
    while True:
        # Handle the choices
        if choice == 1:
            click.echo("\n>>> You chose to build test cases!")
            build_test_cases()
        elif choice == 2:
            click.echo("\n>>> You chose to review your rizz performance!")
            code_review()
        elif choice == 3:
            click.echo("\n>>> You chose to show off your rizz in English!")
            create_documentation()
        elif choice == 4:
            click.echo("\n>>> You chose to refactor your code!")
            refactor_code()
        elif choice == 5:
            click.echo("\nThank you for using our tools!")
            return
        else:
            click.echo("\nInvalid choice. Please run the program again and pick 1-6.")
            return
        
        choice = click.prompt("Do you want to choose another option? (1-5)", type=int)

if __name__ == "__main__":
    menu()
