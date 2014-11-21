import pylab as pl
import numpy as np
import re, tkinter

from tkinter import Label, Entry, Button, Tk


def start(event):
    global tex, a, b, d, e
    tex = ent.get()
    a = entx1.get()
    b = entx2.get()
    d = enty1.get()
    e = enty2.get()


root1 = Tk() # input function and intervals
root1.geometry('+550+400')
lb = Label(root1, text = 'Введите мат.выражение', bg = 'black',fg = 'white',font = 'arial 20')
lb1 = Label(root1, text = 'Введите интервал для x', bg ='black',fg = 'white',font = 'arial 18')
lb2 = Label(root1, text = 'Введите интервал для y', bg = 'black', fg = 'white', font = 'arial 18')
ent = Entry(root1,bd=5)
lb.grid(row = 1, column = 1)
ent.grid(row = 2,column = 1)
lb1.grid(row = 3,column = 1)
entx1=Entry(root1, bd = 5)
entx2=Entry(root1, bd = 5)
entx1.grid(row = 4, column = 0)
entx2.grid(row = 4, column = 2)
lb2.grid(row = 5, column = 1)
enty1=Entry(root1, bd = 5)
enty2=Entry(root1, bd = 5)
enty1.grid(row = 6, column = 0)
enty2.grid(row = 6, column = 2)
bt = Button(root1, text = 'done', width = 10, height = 3, 
            bg = 'black', fg='white', command = root1.destroy)
bt.bind("<Button-1>", start)
bt.grid(row = 7, column = 1)
root1.mainloop()

pre = re.compile('([A-Za-z]+)')
xre = re.compile(r'\bx\b')
notx = re.compile('@')
s = tex
s = xre.sub('@', s)
s = pre.sub(r'np.\1', s)
s = notx.sub('x', s)

pl.figure(figsize=(8, 6), dpi=80)
pl.subplot(1, 1, 1)
x = np.linspace( float(a),float(b),2000, endpoint=True)
C = eval(s)
pl.plot(x, C, color="blue", linewidth=1.0, linestyle="-")
pl.xlim(float(a), float(b))
pl.xticks(np.linspace(float(a), float(b), 5, endpoint=True))
pl.ylim(float(d), float(e))
pl.yticks(np.linspace(float(d), float(e), 5, endpoint=True))
pl.show()
