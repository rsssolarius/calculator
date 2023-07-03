import tkinter as tk
from tkinter import messagebox

# Создание кнопок с цифрами
def make_digit_button(digit):
    return tk.Button(win, text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


# Операция по добавлению цифры при нажатии на кнопку
def add_digit(digit):
    value_calc = calc.get()             # Значение из верхнего поля
    value_field = second_field.get()    # Значение из нижнего поля

    # Mod.1
    if mod_dig == 1:
        if value_calc == '0':
            calc.delete(0, tk.END)
            calc.insert(0, digit)
        else:
            calc.insert(tk.END, digit)
    # Mod.2
    else:
        if value_calc == '0':
            calc.delete(0, tk.END)
            calc.insert(0, digit)
        else:
            calc.insert(tk.END, digit)


# Создание кнопок с операциями
def make_operation_button(operation):
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))


# Нажатие кнопки с операцией
def add_operation(operation):
    value_calc = calc.get()
    value_field = second_field.get()
    # Mod.1
    if mod_dig == 1:
        if value_calc[-1] in '+-*/':
            value_calc = value_calc[:-1]
        calc.delete(0, tk.END)
        calc.insert(0, value_calc + operation)
    # Mod.2
    else:
        if value_field == '0':
            second_field.delete(0, tk.END)
            second_field.insert(0, value_calc + operation)
            calc.delete(0, tk.END)

        elif value_field[-1] in '+-*/' and value_calc == '':
            value_field = value_field[:-1] + operation
            second_field.delete(0, tk.END)
            second_field.insert(0, value_field)
        else:
            calc.delete(0, tk.END)
            second_field.delete(0, tk.END)
            try:
                second_field.insert(0, str(eval(value_field + value_calc)) + operation)
            except (NameError, SyntaxError):
                messagebox.showinfo('Внимание!', 'Допустимо вводить только цифры!')
                calc.insert(0, '0')
                second_field.insert(0, '0')
            except (ZeroDivisionError):
                messagebox.showinfo('Внимание!', 'На 0 делить нельзя!')
                calc.insert(0, '0')
                second_field.insert(0, '0')


# Кнопка "="
def make_calc_button():
    return tk.Button(win, text='=', bd=5, font=('Arial', 13), fg='red',
                     command=calculate)


# Вычисление при нажатии на "="
def calculate():
    value_calc = calc.get()
    value_field = second_field.get()
    if mod_dig == 1:
        if value_calc[-1] in '+-*/':
            value_calc = value_calc + value_calc[:-1]
        calc.delete(0, tk.END)
        try:
            calc.insert(0, eval(value_calc))
        except (NameError, SyntaxError):
            messagebox.showinfo('Внимание!', 'Допустимо вводить только цифры!')
            calc.insert(0, '0')
        except (ZeroDivisionError):
            messagebox.showinfo('Внимание!', 'На 0 делить нельзя!')
            calc.insert(0, '0')

    else:
        if value_field != '0' and value_calc != '':
            calc.delete(0, tk.END)
            second_field.delete(0, tk.END)
            try:
                calc.insert(0, str(eval(value_field + value_calc)))
                second_field.insert(0, '0')
            except (NameError, SyntaxError):
                messagebox.showinfo('Внимание!', 'Допустимо вводить только цифры!')
                calc.insert(0, '0')
                second_field.insert(0, '0')
            except (ZeroDivisionError):
                messagebox.showinfo('Внимание!', 'На 0 делить нельзя!')
                calc.insert(0, '0')
                second_field.insert(0, '0')
        else:
            pass


def make_clear_button():
    return tk.Button(win, text='C', bd=5, font=('Arial', 13), fg='red',
                     command=clear)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    second_field.delete(0, tk.END)
    second_field.insert(0, '0')


# Добавим режим, при котором результат выдается итеративно по операциям (Mod. 2)
mod_dig = 1


def mod():
    global mod_dig
    if mod_dig == 1:
        tk.Button(win, text='Mod.2', command=mod).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='wens')
        second_field.configure(state='normal', readonlybackground='white')
        calc.delete(0, tk.END)
        calc.insert(0, '0')
        second_field.delete(0, tk.END)
        second_field.insert(0, '0')
        mod_dig = 2
    else:
        tk.Button(win, text='Mod.1', command=mod).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='wens')
        second_field.configure(state='normal', readonlybackground='#33ffe6')
        calc.delete(0, tk.END)
        calc.insert(0, '0')
        second_field.delete(0, tk.END)
        second_field.configure(state='readonly', readonlybackground='#33ffe6')
        mod_dig = 1


def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()



win = tk.Tk()
win.geometry('240x315+100+200')
win['bg'] = '#33ffe6'
win.title('Калькулятор')

# Распишем возможные события и привяжем их к функциям
# Ввод с клавиатуры
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=1, column=0, columnspan=4, sticky='we', padx=5, pady=5)

make_digit_button('1').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('2').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('3').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('4').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('5').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('6').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('7').grid(row=4, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('8').grid(row=4, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('9').grid(row=4, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('0').grid(row=5, column=0, sticky='wens', padx=5, pady=5)

make_operation_button('+').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('-').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('/').grid(row=5, column=3, sticky='wens', padx=5, pady=5)

make_calc_button().grid(row=5, column=2, sticky='wens', padx=5, pady=5)
make_clear_button().grid(row=5, column=1, sticky='wens', padx=5, pady=5)

# Кнопка и поле для модификации
tk.Button(win, text='Mod.1', command=mod).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='wens')
second_field = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 10), width=15, state='readonly', readonlybackground='#33ffe6')
second_field.grid(row=0, column=2, columnspan=2, sticky='we', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(0, minsize=30)
win.grid_rowconfigure(1, minsize=30)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.mainloop()
