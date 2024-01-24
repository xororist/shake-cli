#!/bin/bash

echo "[-] Installing Shake CLI [-]"

# Check if Python 3 is correctly installed on the machine
echo "[-] Checking if python3 is installed [-]"
if command -v python3 >/dev/null 2>&1; then
    echo "[OK] Python 3 is installed!"
else
    echo "[ERR] Python 3 has not been found or is not installed..." 
    echo "[ERR] Please install Python 3.7 or above in order to use Shake CLI..."
    echo "[ERR] Exiting..."
    exit 1
fi

# Check if pip3 is installed in order to install dependencies
echo "[-] Checking if pip3 is installed [-]"
if command -v pip3 >/dev/null 2>&1; then
    echo "[OK] pip3 is installed!"
else
    echo "[ERR] pip3 has not been found or is not installed..." 
    echo "[ERR] Please install pip3 in order to install required dependencies for Shake CLI..."
    echo "[ERR] Exiting..."
    exit 1
fi

# Upgrade pip3 to the latest version
echo "[-] Upgrading pip3 to the latest version [-]"
if pip3 install --upgrade pip; then
    echo "[OK] pip3 has been upgraded to the latest version."
else
    echo "[ERR] Please update pip3 to the latest version in order to install required dependencies for Shake CLI..."
    echo "[ERR] Exiting..."
    exit 1
fi

# Install Shake CLI from pyproject.toml
echo "[-] Installing Shake CLI [-]"
if python3 -m pip install .; then
    echo "[-] Shake CLI has been successfully installed! [-]"

    shake_dir="$(python3 -c 'import sysconfig; print(sysconfig.get_paths()["scripts"])')"
    
    # Add the shake command to PATH if it is not already in the ~/.bashrc file
    if [[ ":$PATH:" != *":$shake_dir:"* ]]; then
        echo "export PATH=\"\$PATH:$shake_dir\"" >> ~/.bashrc
        echo "[-] Shake CLI directory has been successfully added to PATH! [-]" 
        echo "[-] Please restart your terminal or run 'source ~/.bashrc' in order to run the Shake CLI. [-]"
    else
        echo "[-] Shake CLI is already registered in PATH [-]"
    fi
    
    echo "[-] Start using it by running the 'shake' command! [-]"
else
    echo "[ERR] Shake CLI installation failed..."
    echo "[ERR] Exiting..."
    exit 1
fi
