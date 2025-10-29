#!/bin/bash

echo "Checking for SUID binaries..."
find / -perm -u=s -type f 2>/dev/null

echo "Checking for writable /etc/passwd..."
ls -l /etc/passwd | grep -e "-w-"

echo "Checking for sudo version..."
sudo -V
