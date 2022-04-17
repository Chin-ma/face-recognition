import os
from tkinter import *
import tkinter as tk
from tkinter import font

from numpy import size
master = Tk()

master.geometry("450x350")
master.title("Face mask detection system")
# canvas = tk.Canvas(master, height=300, width=600)
# canvas.pack()

# def acceptData():
#     newWindow = Toplevel(master)
#     newWindow.title("Add new face data")
#     newWindow.geometry("400x400")
#     inputtxt = tk.Text(newWindow, height=1, width=30, font=buttonFont)
#     inputtxt.pack()
#     lbl = tk.Label(newWindow, text="")
#     lbl.pack()
#     lbl.config(text="Id")
#     faceId = inputtxt.get(1.0, "end-1c")
#     lbl.config(text="Name")
#     faceName = inputtxt.get(1.0, "end-1c")
#     lbl.config(text="Email")
#     faceEmail = inputtxt.get(1.0, "end-1c")


def firstScript():
    os.system('/home/chinmay/face-recognition/sqldata.py')

def secondScript():
    os.system('/home/chinmay/face-recognition/genrate.py')
    
def thirdScript():
    os.system('/home/chinmay/face-recognition/facetrain.py')

buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
fButton = Button(master, text="Start Mask Detection", command=firstScript, font=buttonFont)
fButton.place(x=100, y=25)
sButton = Button(master, text="Add new face", command=secondScript, font=buttonFont)
sButton.place(x=140, y=100)
tButton = Button(master, text="Train model for newly added faces", command=thirdScript, font=buttonFont)
tButton.place(x=40, y=175)
# fButton.pack()
# sButton.pack()
# tButton.pack()

mainloop()