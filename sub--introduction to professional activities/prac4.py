"""Color changer"""

import tkinter as tk # ну типа сама библиотека
from tkinter import messagebox # пачиму та без этого месседж бокс не работаит хезе
from tkinter import ttk


def show_info_about_programm():
    """Showinfo box"""
    messagebox.showinfo("О программе", "ну типа о программе)0)")


def dismiss(window):
    """True destroy window"""
    window.destroy()


def mainwin():
    """Main"""
    def set_color(event):
        frame["background"] = str(colors_combobox.get())

    def set_brightness(event):
        factor = float(brightness_slider.get())
        color = str(colors_combobox.get())
        if color != '':
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)
            darkened_color = "#{:02x}{:02x}{:02x}".format(r, g, b) # Idiot pylint
            print(darkened_color)
            frame["background"] = darkened_color
        else:
            messagebox.showerror("Error!", "U must choose color)0)")


    win = tk.Tk()
    win.title("ColorChanger")
    win.iconbitmap('help_gui/cfg/icon.ico')
    win.geometry("300x200+400+150")
    win.resizable(False, False)
    win.protocol("WM_DELETE_WINDOW", lambda: dismiss(win))


    menu_top = tk.Menu(win)
    win.config(menu = menu_top)

    help_menu = tk.Menu(menu_top, tearoff = 0)
    menu_top.add_cascade(label = 'Справка', menu = help_menu)
    help_menu.add_command(label = 'О программе', command = show_info_about_programm)


    frame = tk.Frame(win, width = 300, height = 200)
    colors_combobox = ttk.Combobox(values=['#FF0000', '#008000', '#FF69B4',
                                           '#FFFF00', '#0000FF', '#800080'], state="readonly")
    brightness_slider = tk.Scale(frame, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)

    frame.pack()
    colors_combobox.place(x=10, y=10, height=30, width=280)
    brightness_slider.place(x=10, y=50, height=40, width=280)
    colors_combobox.bind("<<ComboboxSelected>>", set_color)
    brightness_slider.bind("<ButtonRelease-1>", set_brightness)

    win.mainloop()


mainwin()
