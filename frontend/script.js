const term = new Terminal({
  cursorBlink: true,
  rows: 24,
  fontFamily: "monospace",
  theme: {
    background: "#11111b",
    foreground: "#f8f8f2",
    cursor: "#a6e3a1",
  }
});

term.open(document.getElementById("terminal"));

let currentInput = "";
let currentCwd = "~";
let username = "user";
let hostname = "webhost";

function printPrompt() {
  // use ANSI escape codes for colored prompt
  const green = "\x1b[32m";
  const blue = "\x1b[36m";
  const reset = "\x1b[0m";
  term.write(`\r\n${green}${username}@${hostname}${reset}:${blue}${currentCwd}${reset} $ `);
}

async function initCwd() {
  const res = await runCommand("pwd");
  if (res.cwd) {
    currentCwd = res.cwd;
  }
  printPrompt();
}


async function fetchUserInfo() {
  try {
    const res = await fetch("http://127.0.0.1:8000/info");
    if (res.ok) {
      const data = await res.json();
      username = data.username || username;
      hostname = data.hostname || hostname;
    }
  } catch (e) {
    // fallback to defaults
  }
}

term.write("Welcome to Web Terminal!\r\n");
fetchUserInfo().then(initCwd);

term.onKey(async ({ key, domEvent }) => {
  const printable = !domEvent.altKey && !domEvent.ctrlKey && !domEvent.metaKey;

  if (domEvent.key === "Enter") {
    const cmd = currentInput.trim();
    term.write("\r\n");

    if (cmd.length > 0) {
      if (cmd === "clear") {
        term.clear();
      } else {
        const res = await runCommand(cmd);
        term.write(res.output.replace(/\n/g, "\r\n"));
        currentCwd = res.cwd;
      }
    }

    currentInput = "";
    printPrompt();
  } else if (domEvent.key === "Backspace") {
    if (currentInput.length > 0) {
      currentInput = currentInput.slice(0, -1);
      term.write("\b \b");
    }
  } else if (printable) {
    currentInput += key;
    term.write(key);
  }
});

async function runCommand(cmd) {
  try {
    const res = await fetch("http://127.0.0.1:8000/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command: cmd })
    });
    return await res.json();
  } catch (err) {
    return { output: "Error: Could not reach backend\r\n", cwd: currentCwd };
  }
}
