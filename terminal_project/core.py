import os
from rich.console import Console
from terminal_project.commands.file_ops import handle_file_command
from terminal_project.commands.file_view import handle_view_command
from terminal_project.commands.system_ops import handle_system_command
from terminal_project.commands.utils import show_manual

console = Console()
history_list = []

COMMAND_HANDLERS = {
    # file operations
    "pwd": handle_file_command,
    "ls": handle_file_command,
    "cd": handle_file_command,
    "mkdir": handle_file_command,
    "rm": handle_file_command,
    "mv": handle_file_command,
    "cp": handle_file_command,
    "touch": handle_file_command,

    # file viewing/editing
    "cat": handle_view_command,
    "head": handle_view_command,
    "tail": handle_view_command,
    "echo": handle_view_command,

    # system monitoring
    "cpu": handle_system_command,
    "mem": handle_system_command,
    "ps": handle_system_command,
    "kill": handle_system_command,
    "df": handle_system_command,
    "uptime": handle_system_command,
}


def process_command(cmd: str, capture: bool = False):
    """
    Process a command.
    - capture=True → return (output, cwd)
    - capture=False → print directly to console
    """
    parts = cmd.strip().split()
    if not parts:
        return "" if capture else None

    command, args = parts[0], parts[1:]
    history_list.append(cmd)

    # handle special commands
    if command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        return "" if capture else None

    if command == "man":
        manual_text = show_manual(args, console)
        if capture:
            return manual_text, os.getcwd()
        else:
            console.print(manual_text)
            return

    if command == "history":
        history_output = "\n".join(
            [f"{idx+1}\t{h}" for idx, h in enumerate(history_list)]
        )
        if capture:
            return history_output, os.getcwd()
        else:
            console.print(history_output)
            return

    handler = COMMAND_HANDLERS.get(command)
    if handler:
        if capture:
            from io import StringIO
            import contextlib

            buf = StringIO()
            with contextlib.redirect_stdout(buf):
                handler(command, args, console)
            return buf.getvalue(), os.getcwd()
        else:
            handler(command, args, console)
            return
    else:
        msg = f"Unknown command: {command}"
        if capture:
            return msg, os.getcwd()
        else:
            console.print(msg, style="bold red")
            return
