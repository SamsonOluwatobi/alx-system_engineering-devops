# 0x0B. SSH

This repository contains scripts and configuration files related to SSH setup and configuration tasks.

## Files

### 0-use_a_private_key

A Bash script that uses `ssh` to connect to a server using the private key `~/.ssh/school` with the user `ubuntu`. It demonstrates the usage of `ssh` with single-character flags.

Example usage:
```bash
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$
