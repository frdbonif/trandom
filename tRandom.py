#! /usr/bin/python3

# tRandom (C) Fred Boniface 2020, All Rights Reserved

from tkinter import *
import tkinter.messagebox
import random

class Window(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # Define prevResults list
        self.prevResults = [" ", " ", " ", " "," ", " ", " ", " "]

        # Define Menu Bar
        menu = Menu(self.master)
        self.master.config(menu=menu)
        fileMenu = Menu(menu)
        menu.add_cascade(label="File", menu = fileMenu)
        aboutMenu = Menu(menu)
        menu.add_cascade(label="About", menu=aboutMenu)

        # Define menu emtries
        fileMenu.add_command(label="Exit", command=self.clickExit)
        aboutMenu.add_command(label="Version", command=self.clickVersion)
        aboutMenu.add_command(label='License', command=self.clickLic)
        aboutMenu.add_command(label="About", command=self.clickAbout)

        # Define top labels and entry boxes
        l1 = Label(self, text="Enter the range of numbers below")
        l1.place(x=5,y=10)
        lIn1 = Label(self, text="Lowest Number:")
        lIn1.place(x=5,y=40)
        self.in1 = Entry(self, bd=1, width=7)
        self.in1.place(x=150,y=40)
        self.in1.insert(0,"1")
        lIn2 = Label(self, text="Highest Number:")
        lIn2.place(x=5,y=70)
        self.in2 = Entry(self, bd=1, width=7)
        self.in2.place(x=150, y=70)
        self.in2.insert(0,"100")

        # Define result labels
        self.l3 = Label(self, text="Your result:")
        self.l3.place(x=5,y=100)
        self.l2 = Label(self, font=("Courier", 55), fg="red")
        self.l2.place(x=5,y=130)
        self.l4 = Label(self, text="Past results:")
        self.l4.place(x=160,y=100)
        
        # Define past result labels
        self.past1 = Label(self)
        self.past1.place(x=165,y=120)
        self.past2 = Label(self)
        self.past2.place(x=165,y=140)
        self.past3 = Label(self)
        self.past3.place(x=165,y=160)
        self.past4 = Label(self)
        self.past4.place(x=165,y=180)
        self.past5 = Label(self)
        self.past5.place(x=205,y=120)
        self.past6 = Label(self)
        self.past6.place(x=205,y=140)
        self.past7 = Label(self)
        self.past7.place(x=205,y=160)
        self.past8 = Label(self)
        self.past8.place(x=205,y=180)

        # Define bottom buttons
        exitButton = Button(self, text="Exit", command=self.clickExit)
        exitButton.place(x=5,y=225)

        rollButton = Button(self, text="Generate", command=self.clickGenerate)
        rollButton.place(x=155,y=225)

        resetButton = Button(self, text="Reset", command=self.clickReset)
        resetButton.place(x=75,y=225)

    # Define Functions

    # Exit the program
    def clickExit(self):
        exit()

    # Interger entry error popup
    def intErr(self):
        print("Oops!")
        tkinter.messagebox.showerror('tRandom - Error','Make sure you only enter whole numbers between 0 and 999.')

    # Software version informational popup
    def clickVersion(self):
        tkinter.messagebox.showinfo('tRandom - Version', 'v0.0.1\n(C) Fred Boniface 2020')

    # About informational popup
    def clickAbout(self):
        tkinter.messagebox.showinfo('tRandom - About', 'An easy to use psuedo-random number generator written in Python 3.\n\nFor more information visit:\nhttps://tRandom.fjla.uk/')

    # License informational popup
    def clickLic(self):
        tkinter.messagebox.showinfo('tRandom - License', 'tRandom is licensed under the GPLv3.  A copy of this license is included with the software, for more information visit:\nhttps://trandom.fjla.uk/')

    # Reset function.
    def clickReset(self):
        self.prevResults.clear()
        self.prevResults = [" ", " ", " ", " "," ", " ", " ", " "]
        self.l2.config(text="")
        self.past1.config(text="")
        self.past2.config(text="")
        self.past3.config(text="")
        self.past4.config(text="")
        self.past5.config(text="")
        self.past6.config(text="")
        self.past7.config(text="")
        self.past8.config(text="")

    # Generate function.
    def clickGenerate(self):
        
        # Get strings from entry box
        lowStr = self.in1.get()
        highStr = self.in2.get()
        print("Low: " + lowStr)
        print("High: " + highStr)
        
        # Try to convert strings to intergers or show error box
        try:
            lowInt = int(lowStr)
            highInt = int(highStr)
            highInt += 1
        except:
            self.intErr()

        # Check that the intergers are within range
        if highInt > 1000:
            self.intErr()
        elif lowInt < 0:
            self.intErr()
        else:
            
            # Generate the random number and print to console
            result = random.randrange(lowInt,highInt)
            print("Result:")
            print(result)
        
            # Append to prevResults print list to console
            self.prevResults.append(result)
            print(self.prevResults)

            # Print result and prevResults to interface
            self.l2.config(text=result)
            self.past1.config(text=self.prevResults[-1])
            self.past2.config(text=self.prevResults[-2])
            self.past3.config(text=self.prevResults[-3])
            self.past4.config(text=self.prevResults[-4])
            self.past5.config(text=self.prevResults[-5])
            self.past6.config(text=self.prevResults[-6])
            self.past7.config(text=self.prevResults[-7])
            self.past8.config(text=self.prevResults[-8])

# Main
root = Tk()
app = Window(root)
root.iconphoto(False, PhotoImage(file='icon.png'))
root.wm_title("tRandom")
root.geometry("250x260")
root.mainloop()
