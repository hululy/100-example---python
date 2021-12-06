# 学用tkinter画方形

from tkinter import *

root = Tk()
root.title('Rectangle')
canvas = Canvas(width=400,height=400,bg='yellow')

x0 = 263
y0 = 263
x1 = 275
y1 = 275

for i in range(19):
    canvas.create_rectangle(x0,y0,x1,y1)
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5

canvas.pack(expand=YES,fill=BOTH)
root.mainloop()

