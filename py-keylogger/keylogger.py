#!/usr/bin/python
# -*- coding: utf-8 -*-


import pyxhook


#change this to your log file's path
log_file='./log'


class Lang:
	def __init__(self, name, first, last):
		self.name = name
		self.first = first
		self.last = last

class String:
	def __init__(self, text = "", lang = ""):
		self.text = text
		self.lang = lang

def is_en(c):
	if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
		return (1)

Languages = [
	Lang("en", 'a', 'z'),
	Lang("he", 'א', 'ת')
]

T = []
for lang in Languages:
	T.append(String("", lang.name))

word = String("", "")

def determine_letter(c):
	if (is_en(c)):
		if (c >= 'A' and c <= 'Z'):
			Languages[0].name = "EN"
			return (Languages[0])
		else:
			return (Languages[0])
	elif ():
		for lang in Languages:
			if (c >= lang.first and c <= lang.last):
				return (lang)
	else:
		return ""

def determine_lang(string):
	return ("en")

#this function is called everytime a key is pressed.
def OnKeyPress(event):
	fob=open(log_file,'a')
	c = fob.write(event.Key)
	c = 'a'
	word.text += c

	current_lang = determine_letter(c)
	if (current_lang.name != ""):
		word.lang = current_lang.name
		if (current_lang.name == "EN"):
			c = 'a' + (c - 'A')
			current_lang.name = "en"

		i = 0
		for string in T:
			if (string.lang == lang):
				string.text += c
			else:
				string.text += (int(c) - int(current_lang.first)) + Languages[i].first
			i += 1

	else:

		true_lang = determine_lang(word.text)
		if(true_lang != "" and true_lang != word.lang):
			print("Ctrl A, print out the whole string in the correct language")
			for string in T:
				if (string.lang == true_lang):
					fob.write(string.text)
					fob.write('\n')

		word.text = ""
		
	if (event.Ascii == 96): #96 is the ascii value of the grave key (`)
		fob.close()
		new_hook.cancel()
	return

#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
