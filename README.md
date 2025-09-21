
# Python Terminal Project

A web-based terminal emulator built with FastAPI (Python backend) and a modern JavaScript frontend. It allows users to execute shell-like commands, view system information, and interact with files and processes through a browser interface.

## Features

- **Web Terminal UI**: Modern terminal interface in the browser using xterm.js
- **Backend API**: FastAPI server processes commands and returns output
- **Command Support**: File operations (`ls`, `cd`, `mkdir`, `rm`, etc.), file viewing (`cat`, `head`, `tail`), system monitoring (`cpu`, `mem`, `ps`, `df`, `uptime`), and more
- **Manual Pages**: `man <command>` for help on supported commands
- **Command History**: View previous commands with `history` and use up/down arrows in the browser
- **Cross-platform**: Works on Windows and Unix-like systems

## Project Structure

```
python_terminal/
├── backend/
│   ├── app.py
│   ├── terminal_core.py
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── terminal_project/
│   ├── core.py
│   ├── main.py
│   └── commands/
│       ├── file_ops.py
│       ├── file_view.py
│       ├── system_ops.py
│       ├── utils.py
├── README.md
├── requirements.txt
```

## Getting Started

### Backend

1. **Install dependencies:**
   ```sh
   pip install -r backend/requirements.txt
   pip install -r backend/terminal_project/requirements.txt
   ```
2. **Run the FastAPI server:**
   ```sh
   uvicorn backend.app:app --reload
   ```

### Frontend

Open `frontend/index.html` in your browser. The frontend connects to the backend at `http://127.0.0.1:8000` by default.

## Usage

- Type commands in the web terminal (e.g., `ls`, `cat file.txt`, `cpu`, `man ls`).
- Use `clear` to clear the terminal, `history` to see previous commands, and `exit`/`quit` to leave the CLI (if running locally).
- Use up/down arrows in the browser terminal to navigate command history.

## Requirements

- Python 3.8+
- See `requirements.txt` files for dependencies

## Deployment Notes

- For cloud deployment (e.g., Render), ensure all dependencies are listed and the backend listens on the correct port (from the `PORT` environment variable).
- The backend is OS-agnostic, but some commands may behave differently on Windows vs Linux.
