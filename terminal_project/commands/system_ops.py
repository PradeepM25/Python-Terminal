import psutil
import os
import signal
import time

def handle_system_command(command, args, console):
    try:
        if command == "cpu":
            usage = psutil.cpu_percent(interval=1)
            console.print(f"CPU Usage: {usage}%", style="bold yellow")

        elif command == "mem":
            memory = psutil.virtual_memory()
            console.print(f"Memory Usage: {memory.percent}%", style="bold yellow")

        elif command == "ps":
            console.print("PID\tName\tStatus", style="bold cyan")
            for proc in psutil.process_iter(['pid', 'name', 'status']):
                console.print(f"{proc.info['pid']}\t{proc.info['name']}\t{proc.info['status']}")

        elif command == "kill":
            if not args:
                console.print("Usage: kill <pid>", style="bold red")
            else:
                pid = int(args[0])
                os.kill(pid, signal.SIGTERM)
                console.print(f"Killed process {pid}", style="bold green")

        elif command == "df":
            usage = psutil.disk_usage('/')
            console.print(f"Disk Usage: {usage.percent}% ({usage.used//(1024**3)}GB/{usage.total//(1024**3)}GB)", style="bold yellow")

        elif command == "uptime":
            uptime_seconds = time.time() - psutil.boot_time()
            hours, rem = divmod(int(uptime_seconds), 3600)
            minutes, seconds = divmod(rem, 60)
            console.print(f"Uptime: {hours}h {minutes}m {seconds}s", style="bold yellow")

    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
