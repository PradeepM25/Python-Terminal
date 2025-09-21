# Python Terminal# Python Terminal Project



A web-based terminal emulator built with FastAPI (Python backend) and a modern JavaScript frontend. It allows users to execute shell-like commands, view system information, and interact with files and processes through a browser interface.A web-based terminal emulator built with FastAPI (backend) and a modern JavaScript frontend. It allows users to execute common shell-like commands, view system information, and interact with files and processes through a browser interface.



## Features## Features



- **Web Terminal UI**: Modern terminal interface in the browser using xterm.js- **Web Terminal UI**: Modern terminal interface in the browser using xterm.js

- **Backend API**: FastAPI server processes commands and returns output- **Backend API**: FastAPI server processes commands and returns output

- **Command Support**: File operations (`ls`, `cd`, `mkdir`, `rm`, etc.), file viewing (`cat`, `head`, `tail`), system monitoring (`cpu`, `mem`, `ps`, `df`, `uptime`), and more- **Command Support**: File operations (`ls`, `cd`, `mkdir`, `rm`, etc.), file viewing (`cat`, `head`, `tail`), system monitoring (`cpu`, `mem`, `ps`, `df`, `uptime`), and more

- **Manual Pages**: `man <command>` for help on supported commands- **Manual Pages**: `man <command>` for help on supported commands

- **Command History**: View previous commands with `history` and use up/down arrows in the browser- **Command History**: View previous commands with `history`

- **Cross-platform**: Works on Windows and Unix-like systems- **Cross-platform**: Works on Windows and Unix-like systems



## Project Structure## Project Structure



``````

backend/backend/

  app.py                # FastAPI app, API endpoints  app.py                # FastAPI app, API endpoints

  requirements.txt      # Backend dependencies  requirements.txt      # Backend dependencies

  terminal_core.py      # Command routing for backend  terminal_core.py      # Command routing for backend

  terminal_project/  terminal_project/

    core.py             # Command processing logic    core.py             # Command processing logic

    main.py             # CLI entry point for local terminal    main.py             # CLI entry point for local terminal

    requirements.txt    # Core dependencies    requirements.txt    # Core dependencies

    commands/    commands/

      file_ops.py       # File operation commands      file_ops.py       # File operation commands

      file_view.py      # File viewing commands      file_view.py      # File viewing commands

      system_ops.py     # System monitoring commands      system_ops.py     # System monitoring commands

      utils.py          # Help/manual command      utils.py          # Help/manual command

frontend/frontend/

  index.html            # Main HTML file  index.html            # Main HTML file

  script.js             # Terminal frontend logic (with history navigation)  script.js             # Terminal frontend logic

  style.css             # Styling for terminal UI  style.css             # Styling for terminal UI

``````



## Getting Started## Getting Started



### Backend### Backend



1. **Install dependencies:**1. **Install dependencies:**

   ```sh   ```sh

   pip install -r backend/requirements.txt   pip install -r backend/requirements.txt

   pip install -r backend/terminal_project/requirements.txt   pip install -r backend/terminal_project/requirements.txt

   ```   ```

2. **Run the FastAPI server:**2. **Run the FastAPI server:**

   ```sh   ```sh

   uvicorn backend.app:app --reload   uvicorn backend.app:app --reload

   ```   ```



### Frontend### Frontend



Open `frontend/index.html` in your browser. The frontend connects to the backend at `http://127.0.0.1:8000` by default.Open `frontend/index.html` in your browser. The frontend connects to the backend at `http://127.0.0.1:8000` by default.



## Usage## Usage



- Type commands in the web terminal (e.g., `ls`, `cat file.txt`, `cpu`, `man ls`).- Type commands in the web terminal (e.g., `ls`, `cat file.txt`, `cpu`, `man ls`).

- Use `clear` to clear the terminal, `history` to see previous commands, and `exit`/`quit` to leave the CLI (if running locally).- Use `clear` to clear the terminal, `history` to see previous commands, and `exit`/`quit` to leave the CLI (if running locally).

- Use up/down arrows in the browser terminal to navigate command history.

## Requirements

## Requirements- Python 3.8+

- Python 3.8+- See `requirements.txt` files for dependencies

- See `requirements.txt` files for dependencies

## License

## Deployment NotesMIT License

- For cloud deployment (e.g., Render), ensure all dependencies are listed and the backend listens on the correct port (from the `PORT` environment variable).
- The backend is OS-agnostic, but some commands may behave differently on Windows vs Linux.

## License
MIT License
