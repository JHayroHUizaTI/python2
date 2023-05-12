from tkinter import Tk

from tkinter import *

def main():

    root = Tk()
    root.title("Calculator")
    root.geometry("300x150")
    # frame = ttk.Frame(root, padding="10 10 10 10")
    # frame.grid(column=0, row=0, sticky=(N, W, E, S))
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    root.resizable(0,0)
    root.configure(background = "light green")

    w = Label(root, text='GeeksForGeeks', font="50")
    w.pack()
    frame=Frame(root)
    frame.pack()
    leftframe = Frame(root)
    leftframe.pack(side = LEFT)

    rightframe = Frame(root)
    rightframe.pack(side = RIGHT)

    btn1 = Button(frame, text="Submit", fg="red",activebackground = "red")  
    btn1.pack(side = LEFT)  
  
    btn2 = Button(frame, text="Remove", fg="brown", activebackground = "brown")  
    btn2.pack(side = RIGHT)  

    # uname = Label(root, text ="Username", bg = "blue")
    # uname.grid(row = 0, column = 2)
  
    btn3 = Button(rightframe, text="Add", fg="blue", activebackground = "blue")  
    btn3.pack(side = LEFT)  
  
    btn4 = Button(leftframe, text="Modify", fg="black", activebackground = "white")  
    btn4.pack(side = RIGHT)  
  
    root.mainloop()

if __name__ == '__main__':
    main()