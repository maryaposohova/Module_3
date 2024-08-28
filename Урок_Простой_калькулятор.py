# Простой калькулятор
# Интерфейс
import tkinter as tk  # библиотека тикейинтер, сократили tk, будем делать калькулятор

window = tk.Tk()               # вызвали из библиотеки спец класс, код открывается этой командой
window.title('Калькулятор')    # Переименовали
window.geometry('350x350')     #этим методом задаем размер окна
window.resizable(False, False) # Запрещаем изменять размер, чтобы элементы калькулятора не сбивались (из-за используемого метода)
button_add = tk.Button(window, text='+', width=2, height=2)       #из библиотеки tk создаем команду баттон, и принадлежит она нашему главному окошку виндоу
button_add.place(x=100,y=200)     # разместили созданную кнопку
button_sub = tk.Button(window, text='-', width=2, height=2)
button_sub.place(x=150,y=200)
button_mul = tk.Button(window, text='*', width=2, height=2)
button_mul.place(x=200,y=200)
button_div = tk.Button(window, text='/', width=2, height=2)
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