# Простой калькулятор

import tkinter as tk  # библиотека тикейинтер, сократили tk, будем делать калькулятор

# Функции

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res =num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)



def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)



def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)










# Интерфейс графический
window = tk.Tk()               # вызвали из библиотеки спец класс, код открывается этой командой
window.title('Калькулятор')    # Переименовали
window.geometry('350x350')     #этим методом задаем размер окна
window.resizable(False, False) # Запрещаем изменять размер, чтобы элементы калькулятора не сбивались (из-за используемого метода)
button_add = tk.Button(window, text='+', width=2, height=2, command=add)       #из библиотеки tk создаем команду баттон, и принадлежит она нашему главному окошку виндоу
button_add.place(x=100,y=200)     # разместили созданную кнопку
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=150,y=200)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=200,y=200)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=250,y=200)
number1_entry = tk.Entry(window, width=28)      # делаем 1 поле куда вводить с пом  команды Entry (однострочное текстовое поле) из библиотеки tkinter
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)      # делаем 2 поле куда вводить с пом  команды Entry (однострочное текстовое поле) из библиотеки tkinter
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)      # 3 поле для ответа
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое число')              # 3 лейбл позволяет делать надписи
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число')              # 3 лейбл позволяет делать надписи
number2.place(x=100, y=125)
number2 = tk.Label(window, text='Ответ')               # 3 поле для ответа
number2.place(x=100, y=275)






window.mainloop()              # это должно быть в конце, код закрывается этой командой