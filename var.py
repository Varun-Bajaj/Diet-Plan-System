from tkinter import *
from tkinter.ttk import Progressbar
import time
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
  
root = Tk()
root.geometry('200x150')
  
# function to call when user press
# the save button, a filedialog will
# open and ask to save file
def save():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)

v=Label(root,text="done").pack()
btn = ttk.Button(root, text = 'Save', command = lambda : save())
btn.pack(side = TOP, pady = 20)
  
mainloop()
