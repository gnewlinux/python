#!/usr/bin/env python3
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import webbrowser


### FUNCTIONS
def clickAbout():
    about = Toplevel()
    about.title('About')
    about.geometry('200x100+500+200')
    label1 = Label(about, text='gnew.2017', justify='center')
    label1.pack(padx=10, pady=(25, 10))
    label2 = Label(about, text='good downloads!', justify='center')
    label2.pack(padx=10)

def logo_link():
	webbrowser.open("https://youtube.com")

def open_video():
	os.system('vlc %s' % filename)
	toplevel.destroy()

def download_func():
	url = video.get()
	download.set('Wait...')

	if url != '' and validaUrl(url):
		global filename
		filename = filedialog.asksaveasfilename(filetypes=[("MP4 Files", "*.mp4")])

		os.system('xterm -geometry 95x10+380+510 -sb -e youtube-dl -f mp4 -o %s %s' % (filename, url))

		## STILL NOT RUNNING :(
		progress['value']=20
		root.update_idletasks()
		progress['value']=50
		root.update_idletasks()
		progress['value']=80
		root.update_idletasks()
		progress['value']=100

		## NEW WINDOW
		toplevel = Toplevel()
		toplevel.geometry('200x100')

		label_top = Label(toplevel, text='Download finished.')
		label_top.pack(pady=20)

		btn_top = Button(toplevel, text='OK', command=toplevel.destroy)
		btn_top.pack(side=LEFT, padx=8)

		btn_ver_top = Button(toplevel, text='OPEN', command=open_video)
		btn_ver_top.pack(side=RIGHT, padx=8)

		video.set('')
		progress['value']=0

	else:
		video.set('INVALID URL')

	download.set('Download')

def validaUrl(url):
	ref = 'https://www.youtube.com'
	return url.startswith(ref)

def clear(event):
	video.set('')
	progress['value']=0

def exit():
	root.destroy()


### TK MAIN LOOP
root = Tk()
root.title('tube_down')
root.geometry('220x200')

video = StringVar()

### MENU BAR
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=clickAbout)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar, borderwidth=0, highlightthickness=0)

### WIDGETS
logo = PhotoImage(file='img/youtube.png')
lb_logo = Label(root)
lb_logo['image'] = logo
url = 'https://youtube.com'
lb_logo.bind("<Button-1>",lambda e,url=url:logo_link())
lb_logo.pack()

lb_txt = Label(root, text='Enter URL Youtube: ')
lb_txt.pack()

ed = Entry(root, textvariable=video)
ed.pack()
ed.bind('<Button-1>', clear)

progress=Progressbar(root,orient=HORIZONTAL,length=500,mode='determinate')
progress.pack(side=BOTTOM)

download = StringVar()
download.set('Download')
btn1 = Button(root, textvariable=download, command=download_func)
btn1.pack(side=LEFT, padx=20)

btn2 = Button(root, text='Quit', command=exit)
btn2.pack(side=RIGHT, padx=20)

### LOOP
root.mainloop()