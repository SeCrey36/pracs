"""GUI"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
import backend as bk
import json



def main_window(): 
    def show_info_about_programm():
        messagebox.showinfo("About program",
                            "In this program u can edit airplanes and reservations")

    def dismiss(window):
        window.grab_release()
        window.destroy()

    def delete_airplane():
        try:
            main_thread.del_airplane(planes_combobox.get().split()[0])
            update_combobox()
        except ValueError:
            messagebox.showerror("Error", "0 planes / Not selected")

    def sync_json(frame):
        try:
            data = main_thread.load_json()
            for pl in data:
                info = (pl["name"],
                        len(pl["e_seats"]),
                        int(pl["e_price"]),
                        len(pl["b_seats"]),
                        int(pl["b_price"]),
                        len(pl["f_seats"]),
                        int(pl["f_price"]))
                main_thread.add_airplane(data, info, 1)
            sync_label = tk.Label(frame, text = "Sync done!",
                                font = ("Calibri", 15, "bold"), fg='green', background=color_back)
            sync_label.place(x=10, y=365, height=30, width=100)
        except TypeError:
            messagebox.showerror("Error", "Cannot sync with database")
            sync_label = tk.Label(frame, text = "Error sync",
                                font = ("Calibri", 15, "bold"), fg='red', background=color_back)
            sync_label.place(x=10, y=365, height=30, width=100)
        except json.decoder.JSONDecodeError:
            messagebox.showerror("Error", "Cannot sync with database")
            sync_label = tk.Label(frame, text = "Error sync",
                                font = ("Calibri", 15, "bold"), fg='red', background=color_back)
            sync_label.place(x=10, y=365, height=30, width=100)

    def textbox_print():
        temp = main_thread.plane_info()
        textbox.delete("1.0", "end")
        textbox.insert(1.0, temp)

    def select_plane(event):
        selection = str(planes_combobox.get())
        ind = int(selection.split()[0])
        main_thread.select_airplane(ind)
        textbox_print()

    def update_combobox():
        values = main_thread.list_airplanes()
        planes_combobox["values"] = values
        try:
            planes_combobox.set(values[0])
            select_plane(event=True)
        except IndexError:
            planes_combobox.set('')
            textbox.delete("1.0", "end")
            textbox.insert(1.0, '(Plane info)')

    def new_plane_window():
        def create_plane():
            try:
                info = (name.get(),
                        int(e_seats.get()),
                        int(e_price.get()),
                        int(b_seats.get()),
                        int(b_price.get()),
                        int(f_seats.get()),
                        int(f_price.get()))
                data = main_thread.load_json()
                main_thread.add_airplane(data, info, 0)
                update_combobox()
                dismiss(win_append)
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        win_append = tk.Toplevel(win)
        win_append.title("Append new plane")
        win_append.iconbitmap('sub--basics_of_programming/gui/cfg/icon.ico')
        win_append.geometry("350x260+400+150")
        win_append.resizable(False, False)

        frame2 = tk.Frame(win_append, width=350, height=260, background=color_back)
        name_label = tk.Label(frame2, text = "Name:", background=color_back,
                            justify = 'left', font = ("Calibri", 14, "bold"))
        eco_label = tk.Label(frame2, text = "Eco:", background=color_back,
                            justify = 'left', font = ("Calibri", 14, "bold"))
        busi_label = tk.Label(frame2, text = "Business:", background=color_back,
                            justify = 'left', font = ("Calibri", 14, "bold"))
        first_label = tk.Label(frame2, text = "Elite:", background=color_back,
                            justify = 'left', font = ("Calibri", 14, "bold"))
        count_label = tk.Label(frame2, text = "Count", background=color_back,
                            justify = 'left', font = ("Calibri", 14, "bold"))
        price_label = tk.Label(frame2, text = "Price", background=color_back,
                            justify = 'left', font = ("Calibri", 14, "bold"))
        btn_apply = tk.Button(frame2, text = "Create airplane", font = ("Calibri", 12, "bold"),
                            command = create_plane)

        name = tk.Entry(frame2)
        e_seats = tk.Entry(frame2)
        e_price = tk.Entry(frame2)
        b_seats = tk.Entry(frame2)
        b_price = tk.Entry(frame2)
        f_seats = tk.Entry(frame2)
        f_price = tk.Entry(frame2)

        frame2.pack()
        name_label.place(x=10, y=15, height=25, width=80)
        name.place(x=100, y=15, height=25, width=230)
        e_seats.place(x=100, y=95, height=25, width=110)
        e_price.place(x=220, y=95, height=25, width=110)
        b_seats.place(x=100, y=135, height=25, width=110)
        b_price.place(x=220, y=135, height=25, width=110)
        f_seats.place(x=100, y=175, height=25, width=110)
        f_price.place(x=220, y=175, height=25, width=110)
        count_label.place(x=100, y=55, height=25, width=110)
        price_label.place(x=220, y=55, height=25, width=110)
        eco_label.place(x=10, y=95, height=25, width=80)
        busi_label.place(x=10, y=135, height=25, width=80)
        first_label.place(x=10, y=175, height=25, width=80)
        btn_apply.place(x=20, y=220, height=30, width=310)

        win_append.grab_set()


    def reservation(event):
        def accept_res():
            if seats_combobox.get().split()[1] == 'available':
                main_thread.booking(zone, seats_combobox.get().split()[0])
                messagebox.showinfo("Done", "Seat reserved!")
                textbox_print()
                destroys()

        def del_res():
            if seats_combobox.get().split()[1] == 'reservated':
                main_thread.del_book(zone, seats_combobox.get().split()[0])
                messagebox.showinfo("Done", "Seat unreserved!")
                textbox_print()
                destroys()

        def destroys():
            seats_combobox.destroy()
            bt_reserv.destroy()
            bt_unreserv.destroy()
        
        try:
            zone = int(zones_combobox.get().split()[0])
            seats = main_thread.seats(zone)
            list_seats = []
            for i, seat in enumerate(seats):
                if seat == 0:
                    list_seats.append(str(i)+' available')
                else:
                    list_seats.append(str(i)+' reservated')
            if seats:
                seats_combobox = ttk.Combobox(values = list_seats, state="readonly")
                seats_combobox.place(x=585, y=170, height=30, width=90)
                bt_reserv = tk.Button(frame, text = "Do reservation",
                        font = ("Calibri", 12, "bold"), command = accept_res)
                bt_reserv.place(x=375, y=215, height=30, width=300)
                bt_unreserv = tk.Button(frame, text = "Del reservation",
                        font = ("Calibri", 12, "bold"), command = del_res)
                bt_unreserv.place(x=375, y=245, height=30, width=300)
            else:
                messagebox.showerror("Error", "All seats reserved")
        except AttributeError:
            messagebox.showerror("Error", "Plane not selected")


    win = tk.Tk()
    win.title("AutoAirplane")
    win.iconbitmap('sub--basics_of_programming/gui/cfg/icon.ico')
    win.geometry("700x420+400+150")
    win.resizable(False, False)
    win.minsize(300, 350)
    color_back = '#D8BFD8'
    color_fg = '#E6E6FA'


    

    menuTop = tk.Menu(win)
    win.config(menu = menuTop)

    submenuDown = tk.Menu(menuTop, tearoff = 0)
    menuTop.add_cascade(label = 'Edit', menu = submenuDown)
    submenuDown.add_command(label = 'Append new plane', command = new_plane_window)
    submenuDown.add_separator()
    submenuDown.add_command(label = 'Exit', command = lambda: dismiss(win))

    helpMenu = tk.Menu(menuTop, tearoff = 0)
    menuTop.add_cascade(label = 'Help', menu = helpMenu)
    helpMenu.add_command(label = 'About program', command = show_info_about_programm)




    main_thread = bk.Main()

    frame = tk.Frame(win, width=700, height=400, background=color_back)
    info_label = tk.Label(frame, text = "Information", font = ("Calibri", 15, "bold"),
                    background=color_back)
    airplane_label = tk.Label(frame, text = "Choose airplane:", font = ("Calibri", 15, "bold"),
                    background=color_back)
    booking_label = tk.Label(frame, text = "(Booking) Choose zone:", font = ("Calibri", 15, "bold"),
                    background=color_back)
    textbox = scrolledtext.ScrolledText(frame, background=color_fg, wrap = "word")
    bt_delete = tk.Button(frame, text = "Delete airplane", font = ("Calibri", 12, "bold"),
                        command = delete_airplane)
    sync_json(frame)
    list_airplanes = main_thread.list_airplanes()
    planes_combobox = ttk.Combobox(values = list_airplanes, state="readonly")
    zones_combobox = ttk.Combobox(values = ['1 eco', '2 business', '3 elite'], state="readonly")

    frame.pack()
    info_label.place(x=10, y=5, height=30, width=150)
    airplane_label.place(x=375, y=5, height=30, width=150)
    booking_label.place(x=375, y=140, height=30, width=200)
    textbox.place(x=10, y=35, height=330, width=330)
    textbox.insert(1.0, '(Plane info)')
    bt_delete.place(x=375, y=80, height=30, width=300)
    planes_combobox.place(x=375, y=35, height=30, width=300)
    zones_combobox.place(x=375, y=170, height=30, width=200)
    planes_combobox.bind("<<ComboboxSelected>>", select_plane)
    zones_combobox.bind("<<ComboboxSelected>>", reservation)

    win.mainloop()
