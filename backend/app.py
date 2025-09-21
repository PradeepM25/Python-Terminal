from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import getpass
import socket
from backend.terminal_core import run_command_backend

app = FastAPI()

# allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CommandRequest(BaseModel):
    command: str

@app.post("/run")
def run_command(req: CommandRequest):
    return run_command_backend(req.command)


# New endpoint to get system username and hostname
@app.get("/info")
def get_info():
    username = getpass.getuser()
    hostname = socket.gethostname()
    return {"username": username, "hostname": hostname}
