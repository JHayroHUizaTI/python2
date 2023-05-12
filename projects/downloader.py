from tkinter import *
from pytube import YouTube


def main():

    window=Tk()
    window.geometry("600x300")
    window.resizable(0,0)
    window.title("Youtube Video Downloader")

    lb1 = Label(window,text="Download Youtube video",font='arial 20 bold')
    link=StringVar()
    lb2 = Label(window,text="Paste link", font="arial 15 bold")
    link_enter=Entry(window,width=70,textvariable=link)

    def Downloader():
        url=YouTube(link)
        url=url.streams.get_highest_resolution()
        try:

            url.Download()
            lb3=Label(window, text="Finished downloading", font="arial 15").grid(column=3,row=2)
        except:
            print("An error has occurred")
        print("Download is completed successfully")

    bt1 = Button(window,text="Download video", font="arial 15 bold", bg="pale violet red",padx=2,command=Downloader)
    lb1.grid(column=2,row=0)
    lb2.grid(column=1, row=1)
    link_enter.grid(column=2, row=1)
    bt1.grid(column=1, row=2)

    window.mainloop()

    


if __name__ == "__main__":
    main()
    