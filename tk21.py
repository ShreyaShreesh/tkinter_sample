P13 tk21
import tkinter as tk

root = tk.Tk()
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
strvar.set('Hello World')
en.pack()

root.mainloop()