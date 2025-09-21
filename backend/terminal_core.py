from terminal_project.core import process_command

def run_command_backend(cmd: str):
    output, cwd = process_command(cmd, capture=True)
    return {"output": output, "cwd": cwd}
