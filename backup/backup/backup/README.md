# Week 1 - Day 1: Linux CLI, Users & Permissions

## Navigation & Filesystem Commands, User and Groups, Files Permissions.

| Command | Description | Example |
|---------|-------------|---------|
| `pwd` | Print current working directory | ```bash $ pwd /home/alka``` |
| `ls -la` | List all files in long format with permissions | ```bash $ ls -la total 12 drwxr-xr-x 2 alka alka 4096 Sep 8 17:00 .``` |
| `cd <dir>` | Change directory | ```bash $ cd ~/projects/cloud``` |
| `mkdir -p <path>` | Create directories including parents | ```bash $ mkdir -p ~/projects/cloud/week1``` |
| `touch <file>` | Create empty file | ```bash $ touch notes.txt``` |
| `cp <src> <dst>` | Copy file | ```bash $ cp notes.txt backup.txt``` |
| `mv <src> <dst>` | Move/rename file | ```bash $ mv backup.txt notes.bak``` |
| `rm <file>` | Delete file | ```bash $ rm notes.bak``` |
| `cat <file>` | Display file content | ```bash $ cat notes.txt``` |
| `less <file>` | Scroll through file | ```bash $ less notes.txt``` |
| `head <file>` | Show first 10 lines | ```bash $ head notes.txt``` |
| `tail -f <file>` | Follow last lines | ```bash $ tail -f /var/log/syslog``` |
| `find <dir> -name <pattern>` | Find files | ```bash $ find ~/projects -name "*.txt"``` |
| `grep -r "pattern" <dir>` | Search text in files recursively | ```bash $ grep -r "error" /var/log``` |
| `du -sh <dir>` | Estimate disk usage | ```bash $ du -sh ~/projects``` |
| `df -h` | Show disk space usage | ```bash $ df -h``` |
| `id` | Show user ID and groups | ```bash $ id uid=1000(alka) gid=1000(alka) groups=1000(alka)``` |
| `whoami` | Show current user | ```bash $ whoami alka``` |
| `adduser <username>` | Create new user | ```bash $ sudo adduser devuser``` |
| `usermod -aG <group> <user>` | Add user to group | ```bash $ sudo usermod -aG sudo devuser``` |
| `passwd <user>` | Change password | ```bash $ sudo passwd devuser``` |
| `groups <user>` | List groups of a user | ```bash $ groups devuser``` |
| `sudo <command>` | Run command as superuser | ```bash $ sudo apt update``` |
| `su - <user>` | Switch user | ```bash $ su - devuser``` |
| `chmod <mode> <file>` | Change file permissions | ```bash $ chmod 600 secret.txt``` |
| `chown <user>:<group> <file>` | Change owner & group | ```bash $ chown alka:alka secret.txt``` |
| `chgrp <group> <file>` | Change group | ```bash $ chgrp dev secret.txt``` |
| `umask` | Default permissions for new files | ```bash $ umask``` |
| `suid` | Execute as file owner | ```bash $ chmod u+s file``` |
| `sgid` | Execute as file group | ```bash $ chmod g+s dir``` |
| `sticky` | Only owner can delete files in dir | ```bash $ chmod 1777 /tmp/shared``` |
**Important files**:  
- `/etc/passwd` — user info  
- `/etc/group` — group info  
- `/etc/shadow` — password hashes  
---
# Week 1- Day 2: Bash scripting

## Writing script for backing up files in a folder, Finding error logs, summarising outout of both script in a file.

| Code | Meaning | Output |
|--------|-----------|----------|
| ```#!/bin/bash backed_up=0 for file in ~/linux/*; do  cp -u  "$file"  ~/linux/backup; ((backed_up++)) done echo "Files backed up: $backed_up"``` | This finds the file in given path and copies updated file into respective path while counting the backed up files. | ```Bash $ Files backed up: 6``` |
| ```#!/bin/bash grep -c "error" /var/log/*.log  awk -F: '$2>0'``` | This finds the .log file with given pattern-error while making sure only print out >0. | ```Bash $ File has: 5 errors``` |
| ```#!/bin/bash #pointing the scripts ~/linux/script.sh ~/linux/error_count.sh #capturing output to report file result=$(./script.sh) echo "Backed up completed: $result " >> report.txt result=$(./error_count.sh) echo "File has: $result  errors" >> report.txt``` | This code runs both scripts and summaried the outout in the report file | ```Bash $ files backed up: 6 Error files: 5```
