HELP_TEXTS = {
    "ls": "List directory contents. Usage: ls [path]",
    "cd": "Change directory. Usage: cd <path>",
    "pwd": "Print current working directory",
    "mkdir": "Create directory. Usage: mkdir <dirname>",
    "rm": "Remove file or directory. Usage: rm <file/dir>",
    "mv": "Move or rename. Usage: mv <src> <dst>",
    "cp": "Copy file or directory. Usage: cp <src> <dst>",
    "touch": "Create empty file. Usage: touch <filename>",
    "cat": "View file contents. Usage: cat <filename>",
    "head": "Show first 10 lines. Usage: head <filename>",
    "tail": "Show last 10 lines. Usage: tail <filename>",
    "echo": "Print text or write to file. Usage: echo <text> [> file]",
    "grep": "Search for pattern in file. Usage: grep <pattern> <file>",
    "find": "Find files matching pattern. Usage: find <pattern>",
    "cpu": "Show CPU usage",
    "mem": "Show memory usage",
    "ps": "List running processes",
    "kill": "Kill a process. Usage: kill <pid>",
    "df": "Show disk usage",
    "uptime": "Show system uptime",
    "clear": "Clear the screen",
    "exit": "Exit the terminal",
    "man": "Show manual/help. Usage: man <command>",
    "history": "Show command history. Usage: history [N]",
}

def show_manual(args, console):
    if not args:
        return "Usage: man <command>"
    cmd = args[0]
    help_text = HELP_TEXTS.get(cmd)
    if help_text:
        return f"{cmd}: {help_text}"
    else:
        return f"No manual entry for {cmd}"
