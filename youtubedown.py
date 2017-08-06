import subprocess as sub
import os
import sys
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import webbrowser

def logo():
	webbrowser.open("https://youtube.com")

def play():
	#url = 'https://www.youtube.com/watch?v=XjI889CH9qw&t=1s'
	url = video.get()
	download.set('Wait...')

	if url != '' and validaUrl(url):
		filename = filedialog.asksaveasfilename(filetypes=[("MP4 Files", "*.mp4")])
		toplevel = Toplevel()
		toplevel.geometry('600x300+380+100')
		text = Text(toplevel, height=19, width=84)
		text.pack()

		label_top = Label(toplevel, text='status')
		label_top.pack()
		#sistema = os.system('youtube-dl -f mp4' + url)
		p = sub.Popen(['youtube-dl -f mp4 -o ' + filename + ' ' + url], stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
		progress['value']=20
		janela.update_idletasks()
		progress['value']=50
		janela.update_idletasks()
		progress['value']=80
		janela.update_idletasks()
		progress['value']=100
		output = p.communicate()
		text.insert(END, output)
	else:
		video.set('Url invalida')
	download.set('Download')

def validaUrl(url):
	ref = 'https://www.youtube.com'
	return url.startswith(ref)

def limpar(event):
	video.set('')
	progress['value']=0

def sair():
	janela.destroy()

def clickAbout():
    toplevel = Toplevel()
    toplevel.title('About')
    toplevel.geometry('200x100+500+200')
    label1 = Label(toplevel, text='gnew 2017', width=30)
    label1.pack()
    label2 = Label(toplevel, text='github.com/gnewlinux/', width=30)
    label2.pack()

janela = Tk()
janela.title('tube_down')
janela.geometry('220x200')

video = StringVar()

# MENU BAR
menubar = Menu(janela)
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Save as", command=file_save)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=janela.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=clickAbout)
menubar.add_cascade(label="Help", menu=helpmenu)

janela.config(menu=menubar, borderwidth=0, highlightthickness=0)


## WIDGETS
foto = PhotoImage(file='youtube.png')
lb_logo = Label(janela)
lb_logo['image'] = foto
lb_logo.pack()

lb_txt = Label(janela, text='Enter URL Youtube: ')
lb_txt.pack()

ed = Entry(janela, textvariable=video)
ed.pack()

progress=Progressbar(janela,orient=HORIZONTAL,length=500,mode='determinate')
progress.pack(side=BOTTOM)

download = StringVar()
download.set('Download')
btn1 = Button(janela, textvariable=download, command=play)
btn1.pack(side=LEFT, padx=20)

btn2 = Button(janela, text='Quit', command=sair)
btn2.pack(side=RIGHT, padx=20)

ed.bind('<Button-1>', limpar)


### LOOP
janela.mainloop()