# 用tkinter画椭圆

from tkinter import *

canvas = Canvas(width = 400,height = 600,bg = 'white')

x = 360
y = 160
top = y - 30
bottom = y - 30

for i in range(20):
    canvas.create_oval(250-top, 250-bottom, 250+top, 250+bottom)
    top -= 5
    bottom += 5

canvas.pack()
mainloop()


