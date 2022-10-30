from tkinter import *
from pyautogui import screenshot

window_width = 960
window_height = 540

window = Tk()
window.title("Лабораторна робота №2: Програмування")

canvas = Canvas(window,width=window_width,height=window_height )
w, h = window.winfo_width(), window.winfo_height()
window.geometry("+0+0")
canvas.pack()


file = open("DS3.txt")
for line in file:
    data = line.split(sep=" ")
    x = float(data[0])
    y = float(data[1])
    canvas.create_line(x,y,x+1,y, fill = "green")

window.mainloop()
screenshot('screenshot.png', region = (5,30,window_width,window_height+10))
      