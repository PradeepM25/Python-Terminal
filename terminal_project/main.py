import os
import getpass
import socket
from rich.console import Console
from terminal_project.core import process_command

console = Console()

def main():
    username = getpass.getuser()
    hostname = socket.gethostname()

    while True:
        try:
            cwd = os.getcwd()
            prompt = f"[bold green]{username}@{hostname}[/bold green]:[cyan]{cwd}[/cyan]$ "
            command = console.input(prompt)

            if command in ["exit", "quit"]:
                break
            process_command(command, capture=False)
        except KeyboardInterrupt:
            console.print("\nUse 'exit' or 'quit' to leave.", style="bold yellow")
        except Exception as e:
            console.print(f"Error: {e}", style="bold red")


if __name__ == "__main__":
    main()
