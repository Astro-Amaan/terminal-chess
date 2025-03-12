#!/bin/bash

# Display username watermark
echo "==================================="
echo "  Installing Terminal Chess Game   "
echo "         by Astro-Amaan            "
echo "==================================="
sleep 2

# Ensure Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Installing..."
    sudo apt update && sudo apt install -y python3
fi

# Create a directory for the game
INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"

# Copy the game script
cp chess.py "$INSTALL_DIR/terminal-chess"

# Make it executable
chmod +x "$INSTALL_DIR/terminal-chess"

# Add to PATH if not already present
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$HOME/.bashrc"
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$HOME/.profile"
fi

# Display success message
echo "Installation complete! 🎉"
echo "Run the game using: terminal-chess"
