"""
A simple example of hooking the keyboard on Linux using pyxhook

Any key pressed prints out the keys values, program terminates when spacebar
is pressed.
"""
from __future__ import print_function

# Libraries we need
import pyxhook
import time


# This function is called every time a key is presssed
def kbevent(event, params):
    # print key info
    print(event)
    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 32:
        params['running'] = False

parameters={'running':True}
# Create hookmanager
hookman = pyxhook.HookManager(parameters=True)
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
# Define our parameters for callback function
hookman.KeyDownParameters = parameters
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
while parameters['running']:
    time.sleep(0.1)
# Close the listener when we are done
hookman.cancel()
