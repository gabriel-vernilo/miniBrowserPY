import webbrowser
from tkinter import *

window = Tk()
window.title("Browser / Navegador")
window.geometry("200x80")

def insta():
    webbrowser.open("https://instagram.com", new=2)

def google():
    webbrowser.open("https://google.com", new=2)

def yt():
    webbrowser.open("https://youtube.com", new=2)

def facebook():
    webbrowser.open("https://facebook.com", new=2)

instaButton = Button(window, text="instagram",command=insta).grid(row=1,column=0,padx=10)

googleButton = Button(window, text="google",command=google).grid(row=1,column=1,padx=10)

YTButton = Button(window, text="youtube",command=yt).grid(row=2,column=0,padx=10)

facebutton = Button(window, text="facebook",command=facebook).grid(row=2,column=1,padx=10)

window.mainloop()