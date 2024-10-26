from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from tkinter import filedialog
import os

def new_file():
   global file
   root.title("Untitled-Notepad")
   file=None
   textarea.delete(1.0,END)

def open_file():
  global file
  file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
  if file=="":
      file=None
  else:
      root.title(os.path.basename(file) +"-Notepad")
      textarea.delete(1.0,END)
      f=open(file,'r')
      textarea.insert(1.0,f.read())
      f.close()


def save_file():
   global file
   if file is None:
       file = asksaveasfilename(initialfile='Untitled.txt',
                                defaultextension=".txt",
                                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
   if file:
       with open(file, "w") as f:
           f.write(textarea.get(1.0, END))
       root.title(os.path.basename(file) + "- Notepad")

   else:
       with open(file, "w") as f:
           f.write(textarea.get(1.0, END))



def exit():
    root.destroy()

def cut():
    textarea.event_generate("<<Cut>>")

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")

def about():
 showinfo("Notepad","Notepad By Anjali Mourya ")




root=Tk()
root.geometry("544x625")
root.title("Untitled-Notepad")
root.iconbitmap("Notepad_icon.ico")

#Add TextArea

textarea=Text(root, font="lucida 12")
file=None
textarea.pack(expand=True,fill=BOTH)

#Create MenuBar

Menubar=Menu(root)
FileMenu=Menu(Menubar,tearoff=0)
FileMenu.add_command(label="New" ,command=new_file)
FileMenu.add_command(label="Open",command=open_file)
FileMenu.add_command(label="Save", command=save_file)
FileMenu.add_separator()
FileMenu.add_command(label="Exit" ,command=exit)
Menubar.add_cascade(label="File",menu=FileMenu)


EditMenu=Menu(Menubar,tearoff=0)
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Paste",command=paste)
Menubar.add_cascade(label="Edit",menu=EditMenu)


AboutMenu=Menu(Menubar,tearoff=0)
AboutMenu.add_command(label="About" ,command=about)
Menubar.add_cascade(label="About",menu=AboutMenu)

root.config(menu=Menubar)

#ScrollBar

Scroll=Scrollbar(textarea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=Scroll.set)



root.mainloop()