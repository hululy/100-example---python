# 用tkinter画直线

from tkinter import *

canvas = Canvas(width=300,height=300,bg='skyblue')
canvas.pack(expand=YES, fill=BOTH)

x0 = 263
y0 = 263
x1 = 275
y1 = 275

for i in range(19):
    canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
    x0 -= 5
    y0 -= 5
    y1 += 5

x0 = 268
y0 = 268
y1 = 280

for i in range(29):
    canvas.create_line(x0,y0,x0,y1,fill = 'green')
    x0 += 5
    y0 += 5
    y1 += 5

mainloop()
