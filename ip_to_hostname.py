import socket
import re
import sys
import easygui as gui

sqrl = "\n           )\" .\n         /    \      (\-./\n        /     |    _/ o. \ \n       |      | .-\"      y)-\n       |      |/       _/ \ \n       \     /j   _\".\(@) \n        \   ( |    `.''  )\n         \  _`-     |   /\n           \"  `-._  <_ (\n                  `-.,),)"
print(sqrl)
msg = "Click continue to choose which files to convert or cancel to quit.\n \nIf an ip can't be resolved an error will be thrown but it should continue on with converting."
title = "IP to Hostname"
tf = gui.ccbox(msg, title)
if tf:
	files = gui.fileopenbox(title, multiple = True)
	print(files)
	for file in files:
		f_input = open(file).read()
		for ip in re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', f_input):
			hostname = socket.gethostbyaddr(ip)[0]
			f_input = f_input.replace(ip, hostname)
			update = open(file, "w")
			update.write(f_input)
			update.close()
			print("replaced ip: " + ip + "\nwith Hostname: " + hostname +"\n")
else:
	print("quitting!")
	quit()
