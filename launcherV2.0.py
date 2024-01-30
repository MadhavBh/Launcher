import time as t
import tkinter as tk 
import webbrowser as wb
import requests as r

# BACKEND  	
entries = []
 
def add():
	entry = en.get()
	if entry == "":
		print('hexa')
	else:
		label1 = tk.Label(root, text = entry, fg = 'black')
		label1.pack()
		entries.append(entry)

def clear():
	if len(entries) == 0:
		print('deci')
	else:
		entries.clear()
		label2 = tk.Label(root, text = "-------------The Above Entries Were Deleted--------------", fg = 'red')
		label2.pack()

def execute():                         #this function checks if the site is valid with the current synatax and does the necessary. either open or prints a label.
	if len(entries) == 0:
		print('mal')
	else:
		for i in entries:
			try:
				response = r.get('https://{entry}.com'.format(entry = i))       
				if response.status_code == 200:                                 
					wb.open("https://{entry}.com".format(entry = i))
					print(response.status_code)      
					t.sleep(2)
				else:
					print("site down")
			except r.ConnectionError:
				print("site {i} not reachable or safe or valid".format(i=i))
				label3 = tk.Label(root, text = 'site {i} is either not reachable, safe or valid'.format(i = i), fg = 'orange', bg = 'gray')
				label3.pack()

# -------------------------THE GUI PART STARTS HERE--------------------------- #FRONTEND
root = tk.Tk()
root.title('launcher lite v1.3')

canvas = tk.Canvas(root, height = 50, width = 600)
canvas.pack()

frame = tk.Frame(root, width = 10, height = 10)
frame.pack()

en = tk.Entry(root)
en.pack()

label = tk.Label(frame, height = 3, width = 50, text = 'lable ji')
label.pack()

add = tk.Button(frame, text = 'add', fg = 'green', bg = 'black', command = add)
add.pack()

clear = tk.Button(root, text = 'clear', fg = 'red', bg = 'black', command = clear)
clear.pack()

execute = tk.Button(label, text = 'execute', bg = 'black', fg = 'white', command = execute)
execute.pack()

tk.mainloop()