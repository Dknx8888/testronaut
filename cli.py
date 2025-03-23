import click
import re
from parser import load_pipeline
from pipeoptim_analyzer import analyze_pipeline
from fixer import fix_pipeline, show_diff

@click.group()
def cli():
    """DevOps Pipeline Optimizer CLI"""
    pass

@cli.command()
@click.argument('file', type=click.Path(exists=True))
def analyze(file):
    """Analyze the CI/CD pipeline configuration."""
    pipeline_data = load_pipeline(file)
    suggestions = analyze_pipeline(pipeline_data)

    if suggestions:
        click.echo(click.style("Suggestions for optimization:", bold=True))
        for suggestion in suggestions:
            # Remove Markdown-style bold (**text**) from Gemini output
            cleaned = re.sub(r"\*\*(.*?)\*\*", r"\1", suggestion)
            click.echo(f"- {click.style(cleaned, bold=True)}")
    else:
        click.echo(click.style("No issues found. Your pipeline looks optimized!", bold=True))



@cli.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('-y', 'apply_fix', flag_value=True, default=None, help="Apply fixes automatically without confirmation.")
@click.option('-n', 'apply_fix', flag_value=False, help="Do not apply fixes, just show the diff.")
def fix(file, apply_fix):
    """Automatically fix issues in the CI/CD pipeline configuration and show a diff."""
    pipeline_data = load_pipeline(file)
    original_data = pipeline_data.copy()
    fixed_data = fix_pipeline(pipeline_data)
    diff = show_diff(original_data, fixed_data)

    click.echo(click.style("Proposed Fixes:\n", bold=True))
    click.echo(diff)

    if apply_fix is None:
        # If no flag provided, do nothing (no prompt)
        click.echo(click.style("\nNo action taken. Use '-y' to apply the fix or '-n' to skip it.", fg="yellow"))
    elif apply_fix:
        import yaml
        with open(file, 'w') as stream:
            yaml.dump(fixed_data, stream)
        click.echo(click.style("Fix applied and file updated.", fg="green", bold=True))
    else:
        click.echo(click.style("Fix not applied.", fg="red", bold=True))


if __name__ == '__main__':
    cli()