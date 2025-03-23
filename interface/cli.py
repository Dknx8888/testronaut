import subprocess
import os
import click

@click.command()
def main():
    """
    Launches the Testronaut CLI.
    """
    # Determine the directory where the JavaScript files live.
    js_dir = os.path.dirname(__file__)
    # Use the appropriate file name; if you renamed it, use "index.mjs"
    js_file = os.path.join(js_dir, "index.mjs")
    package_json = os.path.join(js_dir, "package.json")
    node_modules = os.path.join(js_dir, "node_modules")

    # Ensure package.json exists.
    if not os.path.exists(package_json):
        click.echo("❌ package.json not found in the interface directory.")
        return

    # If node_modules doesn't exist, install Node dependencies.
    if not os.path.exists(node_modules):
        click.echo("📦 Installing Node.js dependencies for Testronaut...")
        try:
            subprocess.run(["npm", "install"], cwd=js_dir, check=True)
        except subprocess.CalledProcessError as e:
            click.echo(f"❌ npm install failed: {e}")
            return

    # Now run the Node CLI.
    try:
        subprocess.run(["node", js_file], check=True)
    except FileNotFoundError:
        click.echo("❌ Node.js is not installed or not found in PATH.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error running {os.path.basename(js_file)}: {e}")
