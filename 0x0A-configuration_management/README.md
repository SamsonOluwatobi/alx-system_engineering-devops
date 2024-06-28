# ALX System Engineering DevOps - Configuration Management

This repository contains solutions for the configuration management tasks using Puppet.

## Tasks

### Task 0: Create a File

**Objective:** Create a file at `/tmp/school` with specific permissions, owner, group, and content.

**Puppet Manifest File:** `0-create_a_file.pp`

#### Requirements:
- File path: `/tmp/school`
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File contains: `I love Puppet`

#### Steps:
1. Create the `0-create_a_file.pp` file with the following content:
    ```puppet
    file { '/tmp/school':
      ensure  => 'file',
      content => 'I love Puppet',
      mode    => '0744',
      owner   => 'www-data',
      group   => 'www-data',
    }
    ```

2. Apply the Puppet manifest:
    ```bash
    sudo puppet apply 0-create_a_file.pp
    ```

3. Verify the file:
    ```bash
    ls -l /tmp/school
    cat /tmp/school
    ```

### Task 1: Install a Package

**Objective:** Install Flask version 2.1.0 using `pip3`.

**Puppet Manifest File:** `1-install_a_package.pp`

#### Requirements:
- Install Flask
- Version: `2.1.0`

#### Steps:
1. Create the `1-install_a_package.pp` file with the following content:
    ```puppet
    package { 'flask':
      ensure   => '2.1.0',
      provider => 'pip3',
    }
    ```

2. Apply the Puppet manifest:
    ```bash
    sudo puppet apply 1-install_a_package.pp
    ```

3. Verify the installation:
    ```bash
    flask --version
    ```

### Task 2: Execute a Command

**Objective:** Create a manifest to kill a process named `killmenow` using `pkill`.

**Puppet Manifest File:** `2-execute_a_command.pp`

#### Requirements:
- Must use the exec Puppet resource
- Must use `pkill`

#### Steps:
1. Create the `2-execute_a_command.pp` file with the following content:
    ```puppet
    exec { 'killmenow':
      command => '/usr/bin/pkill -f killmenow',
      onlyif  => '/usr/bin/pgrep -f killmenow',
    }
    ```

2. Run the `killmenow` process in a separate terminal:
    ```bash
    echo -e '#!/bin/bash\nwhile [[ true ]]; do\n  sleep 2\ndone' > killmenow
    chmod +x killmenow
    ./killmenow &
    ```

3. Apply the Puppet manifest:
    ```bash
    sudo puppet apply 2-execute_a_command.pp
    ```

4. Verify the process is terminated:
    ```bash
    pgrep -f killmenow
    ```

## Repository Structure

- `0-create_a_file.pp`: Puppet manifest to create a file.
- `1-install_a_package.pp`: Puppet manifest to install Flask.
- `2-execute_a_command.pp`: Puppet manifest to kill the `killmenow` process.

## Usage

Clone the repository and navigate to the `0x0A-configuration_management` directory to access the Puppet manifests.

```bash
git clone https://SamsonOluwatobi/alx-system_engineering-devops.git
cd alx-system_engineering-devops/0x0A-configuration_management

