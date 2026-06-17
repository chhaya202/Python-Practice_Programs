##this is for importing python GUI
import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#This is for findow property and display
window=tkinter.Tk()
window.geometry("1166x718")
window.title('first python GUI')
window.config(bg='sky blue')

frame = tk.Frame(window,height=900,width=800,bg='white')
frame.place(x=550, y=50)

window.mainloop()


