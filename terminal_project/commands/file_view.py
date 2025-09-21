import os

def handle_view_command(command, args, console):
    try:
        if command == "cat":
            if not args:
                console.print("Usage: cat <filename>", style="bold red")
            else:
                filename = args[0]
                if os.path.isfile(filename):
                    with open(filename, "r") as f:
                        for line in f:
                            console.print(line.rstrip())
                else:
                    console.print(f"No such file: {filename}", style="bold red")

        elif command == "head":
            if not args:
                console.print("Usage: head <filename>", style="bold red")
            else:
                filename = args[0]
                if os.path.isfile(filename):
                    with open(filename, "r") as f:
                        for i, line in enumerate(f):
                            if i == 10:  # first 10 lines
                                break
                            console.print(line.rstrip())
                else:
                    console.print(f"No such file: {filename}", style="bold red")

        elif command == "tail":
            if not args:
                console.print("Usage: tail <filename>", style="bold red")
            else:
                filename = args[0]
                if os.path.isfile(filename):
                    with open(filename, "r") as f:
                        lines = f.readlines()
                        for line in lines[-10:]:
                            console.print(line.rstrip())
                else:
                    console.print(f"No such file: {filename}", style="bold red")

        elif command == "echo":
            if not args:
                console.print("Usage: echo <text> [> filename]", style="bold red")
            else:
                # simple echo (no redirection)
                if ">" in args:
                    idx = args.index(">")
                    text = " ".join(args[:idx])
                    filename = args[idx + 1]
                    with open(filename, "w") as f:
                        f.write(text + "\n")
                    console.print(f"Wrote to {filename}", style="bold green")
                else:
                    console.print(" ".join(args))

    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
