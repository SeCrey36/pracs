"""GUI"""

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import back as bk


def append_salaried(name, salary):
    employee = bk.SalariedEmployee(name, salary)
    company.hire(employee)


def append_hourly(name, hourly_rate, hours):
    employee = bk.HourlyEmployee(name, hourly_rate, hours)
    company.hire(employee)


def append_manager(name, salary, bonus):
    employee = bk.Manager(name, salary, bonus)
    company.hire(employee)


def append_executive(name, salary, bonus, stock_options):
    employee = bk.Executive(name, salary, bonus, stock_options)
    company.hire(employee)


def take_workers_list():
    employee_list = company.show_employees()
    return[str(i + 1) + ' ' + employee_list[i]
           for i in range(len(employee_list))]


def take_worker_info(ind):
    info_arr = company.info(ind - 1)
    return [info_arr[i] for i in range(len(info_arr))]



def donothing():
    print('Done')


def dismiss(window):
    window.grab_release()
    window.destroy()


def show_info_about_programm():
    messagebox.showinfo("О программе", "ну типа о программе)0)")


def openreadme():
    filename = 'help_gui/cfg/guide.txt'
    os.system("start " + filename)


def update_combobox():
    values = take_workers_list()
    workers_combobox["values"] = values
    try:
        workers_combobox.set(values[0])
    except IndexError:
        workers_combobox.set('')



def open_create_win(win, fio):
    def selected(event): # Она вложенная чтобы можно было обратиться к комбобоксу
        def apply_salaried():
            append_salaried(fio_entry.get(), zp_entry.get())
            update_combobox()
            dismiss(win_create)
        def apply_hourly():
            append_hourly(fio_entry.get(), zp_entry.get(), bonus_entry.get())
            update_combobox()
            dismiss(win_create)
        def apply_manager():
            append_manager(fio_entry.get(), zp_entry.get(), bonus_entry.get())
            update_combobox()
            dismiss(win_create)
        def apply_executive():
            append_executive(fio_entry.get(), zp_entry.get(),
                                  bonus_entry.get(), stock_entry.get())
            update_combobox()
            dismiss(win_create)
        selection = combobox.get()
        combobox.destroy()
        info_label.destroy()

        if selection == 'Наёмный':
            type_worker_label = tk.Label(frame2, text = "Наёмный", justify = 'left',
                          font = ("Calibri", 14, "bold"),  background='#00BFFF')
            fio_entry = tk.Entry(frame2)
            fio_entry.insert(0, fio)
            zp_entry = tk.Entry(frame2)
            fio_label = tk.Label(frame2, text = "ФИО", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            zp_label = tk.Label(frame2, text = "ЗП", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            apply_button = tk.Button(frame2, text = "Применить изменения",
                                     font = ("Calibri", 12, "bold"), command = apply_salaried)
            type_worker_label.place(x=10, y=30, height=20, width=330)
            fio_entry.place(x=50, y=55, height=20, width=290)
            zp_entry.place(x=50, y=80, height=20, width=290)
            fio_label.place(x=10, y=55, height=20, width=35)
            zp_label.place(x=10, y=80, height=20, width=35)
            apply_button.place(x=10, y=130, height=30, width=330)

        elif selection == 'Почасовой':
            type_worker_label = tk.Label(frame2, text = "Почасовой", justify = 'left',
                          font = ("Calibri", 14, "bold"),  background='#00BFFF')
            fio_entry = tk.Entry(frame2)
            fio_entry.insert(0, fio)
            zp_entry = tk.Entry(frame2)
            bonus_entry = tk.Entry(frame2)
            fio_label = tk.Label(frame2, text = "ФИО", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            zp_label = tk.Label(frame2, text = "Почасовой", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            bonus_label = tk.Label(frame2, text = "Часы", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            apply_button = tk.Button(frame2, text = "Применить изменения",
                                     font = ("Calibri", 12, "bold"), command = apply_hourly)
            type_worker_label.place(x=10, y=30, height=20, width=330)
            fio_entry.place(x=100, y=55, height=20, width=240)
            zp_entry.place(x=100, y=80, height=20, width=240)
            bonus_entry.place(x=100, y=105, height=20, width=240)
            fio_label.place(x=10, y=55, height=20, width=80)
            zp_label.place(x=10, y=80, height=20, width=80)
            bonus_label.place(x=10, y=105, height=20, width=80)
            apply_button.place(x=10, y=130, height=30, width=330)

        elif selection == 'Менеджер':
            type_worker_label = tk.Label(frame2, text = "Менеджер", justify = 'left',
                          font = ("Calibri", 14, "bold"),  background='#00BFFF')
            fio_entry = tk.Entry(frame2)
            fio_entry.insert(0, fio)
            zp_entry = tk.Entry(frame2)
            bonus_entry = tk.Entry(frame2)
            fio_label = tk.Label(frame2, text = "ФИО", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            zp_label = tk.Label(frame2, text = "Зарплата", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            bonus_label = tk.Label(frame2, text = "Бонус", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            apply_button = tk.Button(frame2, text = "Применить изменения",
                                     font = ("Calibri", 12, "bold"), command = apply_manager)
            type_worker_label.place(x=10, y=30, height=20, width=330)
            fio_entry.place(x=100, y=55, height=20, width=240)
            zp_entry.place(x=100, y=80, height=20, width=240)
            bonus_entry.place(x=100, y=105, height=20, width=240)
            fio_label.place(x=10, y=55, height=20, width=80)
            zp_label.place(x=10, y=80, height=20, width=80)
            bonus_label.place(x=10, y=105, height=20, width=80)
            apply_button.place(x=10, y=130, height=30, width=330)

        else:
            type_worker_label = tk.Label(frame2, text = "Руководитель", justify = 'left',
                          font = ("Calibri", 14, "bold"),  background='#00BFFF')
            fio_entry = tk.Entry(frame2)
            fio_entry.insert(0, fio)
            zp_entry = tk.Entry(frame2)
            bonus_entry = tk.Entry(frame2)
            stock_entry = tk.Entry(frame2)
            fio_label = tk.Label(frame2, text = "ФИО", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            rate_label = tk.Label(frame2, text = "Зарплата", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            hours_label = tk.Label(frame2, text = "Бонус", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            stock_label = tk.Label(frame2, text = "Дивиденты", justify = 'left',
                          font = ("Calibri", 12, "bold"),  background='#00BFFF')
            apply_button = tk.Button(frame2, text = "Применить изменения",
                                     font = ("Calibri", 12, "bold"), command = apply_executive)
            type_worker_label.place(x=10, y=30, height=20, width=330)
            fio_entry.place(x=100, y=55, height=20, width=240)
            zp_entry.place(x=100, y=80, height=20, width=240)
            bonus_entry.place(x=100, y=105, height=20, width=240)
            stock_entry.place(x=100, y=130, height=20, width=240)
            fio_label.place(x=10, y=55, height=20, width=80)
            rate_label.place(x=10, y=80, height=20, width=80)
            hours_label.place(x=10, y=105, height=20, width=80)
            stock_label.place(x=10, y=130, height=20, width=80)
            apply_button.place(x=10, y=155, height=30, width=330)

    win_create = tk.Toplevel(win)
    win_create.title("Редактор сотрудника")
    win_create.iconbitmap('help_gui/cfg/icon.ico')
    win_create.geometry("350x250+400+150")
    win_create.resizable(False, False)

    frame2 = tk.Frame(win_create, width = 350, height = 250,  background='#00BFFF')
    info_label = tk.Label(frame2, text = "Выберите роль", justify = 'left',
                          font = ("Calibri", 14, "bold"),  background='#00BFFF')
    combobox = ttk.Combobox(win_create, values=['Наёмный', 'Почасовой', 'Менеджер', 'Руководитель'],
                                    state="readonly")

    frame2.pack()
    info_label.place(x=10, y=0, height=25, width=150)
    combobox.place(x=10, y=30, height=20, width=330)
    combobox.bind("<<ComboboxSelected>>", selected)

    win_create.grab_set()


def mainwin(workers_list):
    def selected(event): # Она вложенная чтобы можно было обратиться к комбобоксу
        selection = str(workers_combobox.get())
        ind = int(selection.split()[0])
        temp = ''
        try:
            info = take_worker_info(ind)
        except ValueError:
            messagebox.showerror("Ошибка!", "Параметры работника не валидны")
        for i in info:
            temp += i + '\n'
        textbox.delete("1.0", "end")
        textbox.insert(1.0, temp)

    def del_worker():
        try:
            selection = str(workers_combobox.get())
            ind = int(selection.split()[0])
            company.fire(ind - 1)
            update_combobox()
        except IndexError:
            messagebox.showerror("Ошибка!", "Не выбран работник")

    def upgrade_worker():
        try:
            selection = str(workers_combobox.get())
            fio = selection.split()[1]
            ind = int(selection.split()[0])
            open_create_win(win, fio)
            company.fire(ind - 1)
            update_combobox()
        except IndexError:
            messagebox.showerror("Ошибка!", "Не выбран работник")

    global workers_combobox
    global company

    company = bk.Company()

    # НАСТРОЙКА ОКНА
    win = tk.Tk() # обозначаем окно типа виндоу типа вин типа победа это победа друзья
    win.title("Типа название проги") # сверху название
    win.iconbitmap('help_gui/cfg/icon.ico') # путь до иконки надо указывать прям от начала директории проекта
    win.geometry("420x460+400+150") # (ширина х высота + сдвиг от левого верхнего угла моника вправо + вниз)
    win.resizable(False, False) # запретить менять размеры окна
    win.protocol("WM_DELETE_WINDOW", lambda: dismiss(win))

    # МЕНЮ ПРОГРАММЫ
    menu_top = tk.Menu(win)
    win.config(menu = menu_top)

    submenu_down = tk.Menu(menu_top, tearoff = 0)
    menu_top.add_cascade(label = 'Действие', menu = submenu_down)
    submenu_down.add_command(label = 'Добавить нового рабочего',
                             command = lambda: open_create_win(win, ''))
    submenu_down.add_command(label = 'Выход из программы', command = dismiss)

    help_menu = tk.Menu(menu_top, tearoff = 0)
    menu_top.add_cascade(label = 'Справка', menu = help_menu)
    help_menu.add_command(label = 'Иснтрукция по использованию', command = openreadme)
    help_menu.add_separator()
    help_menu.add_command(label = 'О программе', command = show_info_about_programm)

    # ТЕЛО ПРОГРАММЫ
    frame = tk.Frame(win, width = 420, height = 460, background='#00BFFF')


    textbox = scrolledtext.ScrolledText(frame, font = ("Calibri", 12), wrap = "word",
                                        height = 10, background = '#E0FFFF')
    textbox.insert(1.0, 'Здесь будет выводиться информация по рабочим')
    btn_upgrade = tk.Button(frame, text = "Повысить рабочего", font = ("Calibri", 12, "bold"),
                             background = '#B0E0E6', command = upgrade_worker)
    btn_del = tk.Button(frame, text = "Удалить рабочего", font = ("Calibri", 12, "bold"),
                           background = '#B0E0E6', command = del_worker)
    workers_combobox = ttk.Combobox(values=workers_list, state="readonly")

    frame.pack()
    textbox.place(x=10, y=10, height=300, width=400)
    btn_upgrade.place(x=10, y=360, height=30, width=400)
    btn_del.place(x=10, y=400, height=30, width=400)
    workers_combobox.place(x=10, y=320, height=30, width=400)
    workers_combobox.bind("<<ComboboxSelected>>", selected)

    win.mainloop()
