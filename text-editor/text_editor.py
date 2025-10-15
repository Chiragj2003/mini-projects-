from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename


stimulator_window = Tk()
stimulator_window.geometry('600x600') 
stimulator_window.title('TEXT EDITOR')

heading = Label(stimulator_window,text='Welcome to the Text Editor',font=('bold',20),bg='light grey')  # This will creat a label for the heading.
heading.pack()

scrollbar = Scrollbar(stimulator_window)

scrollbar.pack(side=RIGHT,
			fill=Y)


text_info = Text(stimulator_window,
				yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

scrollbar.config(command=text_info.yview)

def save():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_info.get(1.0, tk.END)
        output_file.write(text)
    stimulator_window.title(f"Text Editor - {filepath}")

button = Button(stimulator_window, text='Save', font=('normal', 10), command=save, bg='yellow')
button.place(x=270,y=520)

stimulator_window.mainloop()