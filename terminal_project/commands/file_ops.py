import os
import shutil
import fnmatch

def handle_file_command(command, args, console):
    try:
        if command == "pwd":
            console.print(os.getcwd(), style="bold green")

        elif command == "ls":
            path = args[0] if args else "."
            if os.path.exists(path):
                for item in os.listdir(path):
                    style = "cyan" if os.path.isdir(os.path.join(path, item)) else "white"
                    console.print(item, style=style)
            else:
                console.print(f"No such directory: {path}", style="bold red")

        elif command == "cd":
            if not args:
                console.print("Usage: cd <directory>", style="bold red")
            else:
                target = args[0]
                if os.path.isdir(target):
                    os.chdir(target)
                else:
                    console.print(f"No such directory: {target}", style="bold red")

        elif command == "mkdir":
            if not args:
                console.print("Usage: mkdir <dirname>", style="bold red")
            else:
                os.mkdir(args[0])
                console.print(f"Directory '{args[0]}' created", style="bold green")

        elif command == "rm":
            if not args:
                console.print("Usage: rm <file/dir>", style="bold red")
            else:
                target = args[0]
                if os.path.isdir(target):
                    shutil.rmtree(target)
                    console.print(f"Directory '{target}' removed", style="bold green")
                elif os.path.isfile(target):
                    os.remove(target)
                    console.print(f"File '{target}' removed", style="bold green")
                else:
                    console.print(f"'{target}' not found", style="bold red")

        elif command == "mv":
            if len(args) < 2:
                console.print("Usage: mv <source> <destination>", style="bold red")
            else:
                shutil.move(args[0], args[1])
                console.print(f"Moved {args[0]} -> {args[1]}", style="bold green")

        elif command == "cp":
            if len(args) < 2:
                console.print("Usage: cp <source> <destination>", style="bold red")
            else:
                src, dst = args[0], args[1]
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
                console.print(f"Copied {src} -> {dst}", style="bold green")

        elif command == "touch":
            if not args:
                console.print("Usage: touch <filename>", style="bold red")
            else:
                with open(args[0], "a"):
                    os.utime(args[0], None)
                console.print(f"File '{args[0]}' created", style="bold green")

        elif command == "grep":
            if len(args) < 2:
                console.print("Usage: grep <pattern> <file>", style="bold red")
            else:
                pattern, filename = args[0], args[1]
                if os.path.isfile(filename):
                    with open(filename, "r") as f:
                        for line in f:
                            if pattern in line:
                                console.print(line.rstrip(), style="yellow")
                else:
                    console.print(f"No such file: {filename}", style="bold red")

        elif command == "find":
            if not args:
                console.print("Usage: find <pattern>", style="bold red")
            else:
                pattern = args[0]
                for root, dirs, files in os.walk("."):
                    for name in fnmatch.filter(files, pattern):
                        console.print(os.path.join(root, name), style="cyan")

    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
