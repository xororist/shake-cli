# Shake

## Overview

Shake is an open-source command-line interface (CLI) tool designed for effortless monitoring of resources consumed by a process. It provides a convenient way to track and analyze resource usage, making it a valuable tool for developers and system administrators.

## Project Information

- **Name:** Shake
- **Requires Python:** >= 3.7
- **Keywords:** CLI, monitoring
- **License:** MIT License

## Installation

To install Shake, execute the following commands in your terminal:

```bash
git clone https://github.com/hugo-cachon/shake-cli.git
cd shake-cli
python3 -m pip install .
```

## Basic usage

### Finding Processes

To retrieve a list of all processes running in the environment, use the following command:
```bash
shake find
```
Ouput:
```bash
[-] Pid:     1 | Name: systemd
[-] Pid:     2 | Name: kthreadd
[-] Pid:     3 | Name: pool_workqueue_release
...

```
To find a specific process by its name, use:
```bash
shake find <name>
```
Ouput:
```bash
[-] Pid: 101010 
[-] Name: <name> 
[-] Is running: bool
```

### Monitoring Processes

Initiate the monitoring of a specific process using:
```bash
shake run <pid>
```
Ouput:
```bash
[-] Name: <name> 
[-] Memory Usage: 650.582 MB 
[-] CPU Usage: 1.90%
```

For more detailed information about arguments or options, feel free to use the --help command at any time.

### License

This project is licensed under the MIT License - see the [LICENCE](https://github.com/hugo-cachon/shake-cli/blob/master/LICENCE) file for details.

### Acknowledgments

Thanks to the contributors who make Shake better with their valuable input and feedback.


