# 0. Strace is Your Friend

## Overview

In this project, you'll use `strace` to diagnose why Apache is returning a 500 Internal Server Error. Once you identify the issue, you'll fix it and automate the resolution using Puppet.

## Requirements

1. **Debugging with `strace`**:
   - Use `strace` to attach to the running Apache process and find out why it's returning a 500 error.
   - Use `tmux` to run `strace` in one window and `curl` in another to trigger the error and observe the output.

2. **Fixing the Issue**:
   - Once you've identified the cause of the error using `strace`, create a Puppet manifest to automate the fix.

3. **Puppet Manifest**:
   - Your Puppet manifest should be named `0-strace_is_your_friend.pp`.
   - It should contain Puppet code to fix the issue found.

## Steps to Follow

### 1. Diagnose the Issue with `strace`

1. **Identify the Apache Process**:
   - Find the process ID (PID) of the Apache process:
     ```bash
     ps aux | grep apache2
     ```

2. **Attach `strace` to Apache**:
   - Use `strace` to monitor the Apache process:
     ```bash
     strace -p <PID> -o /tmp/strace_output.txt
     ```

3. **Trigger the Error**:
   - In another terminal, use `curl` to trigger the 500 error:
     ```bash
     curl -sI http://127.0.0.1
     ```

4. **Analyze the Output**:
   - Check `/tmp/strace_output.txt` for clues about the error.

### 2. Create the Puppet Manifest

Based on the findings from `strace`, create a Puppet manifest to automate the fix. For example, if the issue was a typo in a WordPress configuration file, you can use the following Puppet code:

```puppet
# fix wordpress
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}

