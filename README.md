# Building a Simple Keylogger in Python

This blog post will walk you through creating a basic keylogger using Python and the `pynput` library. This is intended for **educational purposes only**. Remember, keyloggers should only be used responsibly and legally on systems you own or have permission to monitor.

## Project Overview

A keylogger records keystrokes on a computer and logs them into a file. We’ll build a basic keylogger that:
- Listens for keyboard events.
- Logs each keystroke with a timestamp.
- Saves the logs to a file (`keylog.txt`).

## Prerequisites

You’ll need:
- **Python** installed (preferably version 3.6 or newer).
- A basic understanding of Python and setting up virtual environments.
- **pynput library**, which allows us to listen to keyboard events.

## Step-by-Step Guide

### Step 1: Set Up the Project Folder

1. **Create a Project Folder**: Make a new directory (e.g., `Keylogger`) for this project.
2. **Open Your Folder in VS Code** (or any editor of your choice).

### Step 2: Create a Virtual Environment

Setting up a virtual environment keeps dependencies organized and separated from other projects.

1. **Create Virtual Environment**: In your terminal, navigate to your project folder and run:
   ```bash
   python -m venv venv
