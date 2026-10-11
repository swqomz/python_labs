import math #from math import sqrt
from math import* 
import random
import statistics as st
from datetime import datetime, date
import demo
from tkinter import *


# a = 81
# print(math.sqrt(a)) #print(sqrt(a))

# grades = [10, 7, 9, 2, 11]
# print(f'середній бал {st.mean(grades)}')
# print(f'mode {st.mode(grades)}')
# print(f'mediana {st.median(grades)}')

# radius = 5
# print(f'circle area: {round((pi * (pow(radius, 2))), 2)}')

# b = 2.45943883
# print(ceil(b))
# print(floor(b))

# balls = 25
# items = 6

# print(f'повністю заповнені коробки {floor(balls / items)}')
# print(f'коробок потрібно всього {ceil(balls / items)}')

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1, 100))

# print(numbers)

# names = ['ivan', 'metvey', 'maria', 'ann']
# print(random.choice(names))

# print(f'today is {datetime.today()}')
# print(f'now is {datetime.now()}')

# year = 2026
# day = 31
# month = 12

# user_day = datetime.today()


# print(demo.squre(5))
# grades2 = [10, 7, 9, 2, 11]
# print(demo.average(grades2))

def text():
    text = 'Welcome to the game'
    label2['text'] = text

def clear(event):
    label2['text'] = ""

window = Tk()
window.title('my first program')
window.geometry('500x500')
window.resizable(width=True, height=False)
# window.configure(background='white')
window["bg"] = 'purple'
label = Label(window, text="My first program", bg='purple', font=('Arial', 25))
# label.pack()
# label.place(x=100, y=200)
label.grid(row=0,column=0, columnspan=2)

bt1 = Button(window, text = 'ok', font = ('Arial', 20),width = 8, activebackground='pink', command=text)
bt1.grid(row=2, column=0, pady=20, padx=10)

bt2 = Button(window, text ='cancel', font = ('Arial', 20), width = 8, activebackground='pink' )
bt2.grid(row=2, column=1, pady=20, padx=10)
bt2.bind('<Button-1>', clear)


label2 = Label(window, text = '',  bg='purple', font=('Arial', 25))
label2.grid(row=3, column=0, columnspan=2)


window.mainloop()