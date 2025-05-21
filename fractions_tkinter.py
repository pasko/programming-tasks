#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

'''
Задание 1: Запрограммировать функцию add_fractions().

Функция add_fractions() должна подсчитать сумму двух дробей, заданных целыми
числами:

   numerator1     numerator2
   ------------ + ------------
   denominator1   denominator2

На английском:
  numerator - числитель
  denominator - знаменатель

Чтобы отобразить полученные числитель и знаменатель, использовать функции
set_result_numerator() и set_result_denominator().

Например, при вычислении суммы:

   1   1
   - + -
   2   4

должно получиться три четверти. Для отображения функция add_fractions() должна
сделать такие действия:

  set_result_numerator(3)
  set_result_denominator(4)

Остальная часть программы отображает 'графический интерфейс' для ввода дробей и
вывода результата. Можно исправить в нём ошибки, если найдутся :)

===

Задание 2: Улучшить функцию add_fractions() так, чтобы перед отображением
результата дробь была максимально 'сокращена'. То есть, получившииеся числитель
и знаменатель нужно разделить на Наибольший Общий Делитель (НОК) этих двух целых
чисел.

Например, при вычислении такой суммы:

  3   1
  - + -
  8   8

должен получиться предварительный результат:

  4
  -
  8

, потом этот результат нужно сократить до:

  1
  -
  2

Как это сделать? Самый простой способ - это разделить 'с остатком' на все числа
от 1 до числителя. Максимальное число, делящее и числитель и знаменатель с
остатком 0 (то есть, без остатка) будет главной находкой. Разделить числитель и
знаменатель на эту "находку", получится нужный результат.

===

Задание 3 (сложное): Использовать Алгоритм Эвклида для нахождения НОК.

===

Задание 4 (по-другому сложное): Научить программу умножать.

Для начала сделать функцию multiply_fractions() с теми же параметрами,
вычисляющую результат умножения двух дробей. Заменить вызов функции
add_fractions() на вызов новой функции.

Далее, заменить символ '+' в программе на кнопку со знаком '+'. При нажатии этой
кнопки знак меняется на '*' и обозначает умножение. Повторное нажатие чередует
отображённый символ между '+' и '*'. Изменить программу так, чтобы при
выбранном символе '+' выполнялась функция add_fractions(), а при выбранном '*'
выполнялось умножение при помощи новой функции multiply_fractions().
'''

def add_fractions(numerator1, denominator1, numerator2, denominator2,
                  set_result_numerator, set_result_denominator):
   ''' Adds two fractions and sets numerator and denominator.

   Uses the provided set_result_enumerator() and set_result_denominator()
   functions to set the numerator and denominator of the result.
   '''
   print('numerator1:', numerator1, ', denominator1:', denominator1)
   print('numerator2:', numerator2, ', denominator2:', denominator2)
   set_result_numerator(123)
   set_result_denominator(321)


def create_ui():
    root = tk.Tk()
    root.title('Input Fields')

    # Use a frame to organize the input fields.
    input_frame = tk.Frame(root)
    input_frame.pack(pady=20)

    # List to store tk.Entry widgets.
    entries = []

    def button_handler():
        values = [entry.get() for entry in entries]
        for i in [0, 1, 3, 4]:
            try:
                int(values[i]) # Try to convert the first value to an integer
            except ValueError:
                messagebox.showerror('Ошибка', 'Введите числа')
                return

        def set_entry(entry, value):
            entry.delete(0, tk.END)
            entry.insert(0, str(value))

        def set_numerator(value : int):
            set_entry(entries[2], value)

        def set_denominator(value : int):
            set_entry(entries[5], value)

        add_fractions(int(values[0]), int(values[3]), int(values[1]),
                      int(values[4]), set_numerator, set_denominator)

    # Create 3 input fields in the first row, leave two empty spaces.
    for i in range(5):
        if i == 1 or i == 3:
            continue
        # width=6 for 4 digits + some padding.
        entry = tk.Entry(input_frame, width=6, justify='center')
        entry.grid(row=0, column=i, padx=10, pady=5)
        entries.append(entry)

    # Add three separators and two signs: '+' and '='.
    for i in range(5):
        if i == 1:
            plus_label = tk.Label(input_frame, text='+')
            plus_label.grid(row=1, column=i, padx=10, pady=0, sticky='ew')
        elif i == 3:
            submit_button = tk.Button(input_frame, text='=', command=button_handler)
            submit_button.grid(row=1, column=i, padx=10, pady=0, sticky='ew')
        else:
            separator = ttk.Separator(input_frame, orient='horizontal')
            separator.grid(row=1, column=i, padx=10, pady=0, columnspan=1, sticky='ew')

    # Create 3 input fields in the second row. Again, with two empty spaces.
    for i in range(5):
        if i == 1 or i == 3:
            continue
        entry = tk.Entry(input_frame, width=6, justify='center')
        entry.grid(row=2, column=i, padx=10, pady=5)
        entries.append(entry)

    # Bind the Escape key to closing the window.
    def close_window_handler(event):
        root.destroy()
    root.bind('<Escape>', close_window_handler)

    return root


def main():
    root = create_ui()
    root.mainloop()


if __name__ == '__main__':
    main()
