import sys
import click
from analyzer import analyze_file
from gemini_api import get_gemini_response


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def refactor(filename):
    results = []
    results.append(f"# Refactoring Suggestions for {filename}\n")
    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()
    results.append(f"Analyzing {filename}...\n")

# Analyze functions
    functions, classes = analyze_file(filename)
    for func_name, snippet in functions:
        results.append(f"\n## Analyzing function: {func_name}\n")
        prompt = (f"Analyze the Python function and suggest refactoring improvements. Make it consise and within 100 words. Do not include the code snippet in the response.")
        suggestion = get_gemini_response(prompt)
        results.append(suggestion + "\n")
# Analyze classes
    for class_name, snippet in classes:
        results.append(f"\n## Analyzing class: {class_name}\n")
        prompt = (f"Analyze the Python class and suggest refactoring improvements. Make it consise and within 100 words. Do not include the code snippet in the response.")
        suggestion = get_gemini_response(prompt)
        results.append(suggestion + "\n")
# Save results to file
    with open("results.md", "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(results))
    click.echo("Refactoring suggestions saved to results.md")



if __name__ == "__main__":
    refactor()
