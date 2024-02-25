### LIBRARY ###

from tkinter import *
from tkinter import ttk, font

def centreWindow(parent):
    w = 800
    h = 600
    sw = parent.winfo_screenwidth()
    sh = parent.winfo_screenheight()
    x = (sw - w) // 2
    y = (sh - h) // 2
    parent.geometry(f'{w}x{h}+{x}+{y}')

def genericHeadLabel(frame, font):
    genericLabel = Label(
            frame,
            text='SIERRA\nBANK',
            font=font,
            justify=LEFT,
            bg='#002441',
            fg='#F3F4EA')
    return genericLabel

def subHeadLabel(frame, font, text):
    subHeadLabel = Label(
            frame,
            text=text,
            font=font,
            justify=RIGHT,
            bg='#002441',
            fg='#F3F4EA')
    return subHeadLabel
    

# HOME BUTTONS #

def homeButton(frame, font, text, bg, command, activebg = None):
    homeButton = Button(
            frame,
            text=text,
            relief=FLAT,
            bg=bg,
            fg='#002441',
            font=font,
            anchor=E,
            padx=20,
            borderwidth=0,
            activebackground=activebg,
            activeforeground="#FFFFFF",
            command=command)
    return homeButton


def genericLabel(frame=None, text=None, font=None):
    caaLabel = Label(
            frame,
            text=text,
            font=font,
            anchor=E,
            bg='#002441',
            fg='#F3F4EA')
    return caaLabel

def genericButton(frame=None, text=None, font=None, command=None):
    button = Button(
            frame,
            text=text,
            relief=FLAT,
            bg='#7F9BA8',
            fg='#F3F4EA',
            anchor=CENTER,
            font=font,
            command=command)
    return button

def backButton(frame=None, font=None, command=None):
    backButton = Button(
            frame,
            text='< Back',
            font=font,
            anchor=W,
            relief=FLAT,
            bg='#002441',
            fg='#F3F4EA',
            borderwidth=0,
            activebackground="#002441",
            activeforeground="#203657",
            command=command)
    return backButton