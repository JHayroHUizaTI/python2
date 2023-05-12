from tkinter import *

def main():

    window = Tk()
    window.title("GUI")
    window.geometry("300x300")
    window.config(bg='#223441')
    window.resizable(0,0)
    lab1 = Label(window,text="Welcome!!", bg="light green")
    lab2 = Label(window, text="Text will pop-up here")
    def clicked():
        lab2.configure(text=e.get())
    e = Entry(window,width=10)
    bt = Button(window,text="Enter",command=clicked)
    lab1.grid(column=1,row=1)
    lab2.grid(column=0,row=2)
    e.grid(column=2, row=2)
    bt.grid(column=0, row=3)

    window.mainloop()


if __name__ == '__main__':
    main()