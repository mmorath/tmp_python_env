#!/bin/bash

# Prompt the user for permission before proceeding with the installation.
echo "Requesting permission to install Poetry on your system."
read -p "Do you want to continue with the installation? (y/n) " -n 1 -r
echo # Move to a new line

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Installation aborted by the user."
    exit 1
fi

echo "Permission granted by the user. Starting the installation process."

# Record the start time to calculate the duration of the script.
start_time=$(date +%s)

# Specify the Poetry version to install.
poetry_version="1.1.13"  # Replace with the desired version of Poetry

# Checking the OS type and version for compatibility.
echo "Checking the operating system compatibility..."
. /etc/os-release
if [[ "$NAME" != "Ubuntu" ]]; then
    echo "This installation script is intended for Ubuntu. You are running $NAME. Exiting..."
    exit 1
fi

# Update the package list to ensure the availability of the latest packages.
echo "Updating the package list..."
sudo apt-get update

# Install prerequisites that are not related to Python, but necessary for Poetry.
echo "Installing system prerequisites..."
sudo apt-get install -y curl git

# Install Python's package management tools.
echo "Installing Python's pip and venv..."
sudo apt-get install -y python3-pip python3-venv

# Downloading and installing the specified version of Poetry.
echo "Installing Poetry version $poetry_version..."
curl -sSL https://install.python-poetry.org | python3 - --version $poetry_version

# Adding Poetry to the system PATH if not already present.
echo "Adding Poetry to the system PATH..."
POETRY_HOME="$HOME/.poetry"
if [[ ! ":$PATH:" == *":$POETRY_HOME/bin:"* ]]; then
    echo "export PATH=\$PATH:$POETRY_HOME/bin" >> $HOME/.profile
    echo "Poetry path added to system PATH."
fi

# Reload the .profile to make the new PATH available in the current session.
echo "Reloading the .profile to update PATH..."
source $HOME/.profile

# Record the end time to calculate the duration of the script.
end_time=$(date +%s)

# Calculate the total duration of the installation.
duration=$((end_time - start_time))

echo "Poetry version $poetry_version installed successfully in $duration seconds."
echo "Please restart your terminal or run 'source ~/.profile' to use Poetry."
