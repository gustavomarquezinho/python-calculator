import sv_ttk as sun_valley
from calcs import Calcs

from tkinter.ttk import (
    Frame,
    Entry,
    Button
)

from tkinter import Tk, PhotoImage


chars = (
    'C', '(', ')', '<',
    '7', '8', '9', '÷',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', ',', '=', '+'
)


class Gui(Tk):
    def __init__(self, title: str):
        super().__init__()

        self.center_window(312, 436)
        self.resizable(0, 0)
        self.title(title)

        sun_valley.set_theme('light')
        self.buttons = []

        self.load_entry()
        self.load_buttons()

        self.iconphoto(False, PhotoImage(file='./calculator/assets/icon_small.png'))


    def center_window(self, size_x: int, size_y: int) -> None:
        pos_x = (self.winfo_screenwidth() / 2) - (size_x / 2)
        pos_y = (self.winfo_screenheight() / 2) - (size_y / 2)

        self.geometry('{}x{}+{}+{}' .format(size_x, size_y, int(pos_x), int(pos_y)))


    def load_entry(self) -> None:
        frame_entry = Frame(self).grid()

        self.entry = Entry(
            master=frame_entry,
            justify='center',
            width=37,
        )

        self.entry.grid(row=0, columnspan=4, padx=(18, 0), pady=(20, 5), ipady=8)


    def load_buttons(self) -> None:
        frame_button, col, row = Frame(self).grid(), 0, 1

        for index, char in enumerate(chars):
            padx = (18, 2) if col == 0 else (2, 2)
 
            self.buttons.append(
                Button(frame_button, text=char, width=6, style='my.TButton')
            )

            self.buttons[len(self.buttons) - 1].grid(
                column=col,
                row=row,
                padx=padx,
                pady=2,
                ipady=16
            )
    
            if (index + 1) % 4 != 0:
                col += 1
                continue

            col, row = 0, row + 1


        for index in range(len(self.buttons)):
            self.set_button_command(index)
        

    def set_button_command(self, index) -> None:
        self.buttons[index]['command'] = lambda: self.on_button_clicked(chars[index])


    def on_button_clicked(self, button) -> None:
        entry_length = len(self.entry.get())

        match button:
            case 'C':
                if entry_length >= 1:
                    self.entry.delete(0, entry_length)

            case '<':
                if entry_length >= 1:
                    self.entry.delete(entry_length - 1)

            case '=':
                calcs = Calcs(self.entry.get())

                self.on_button_clicked('C')
                self.entry.insert(0, calcs.get_formatted())

            case _:
                self.entry.insert(entry_length, button)


    def show_entry_message(self, message: str) -> None:
        self.on_button_clicked('C')

        self.entry.insert(0, message)
        self.entry.select_range(0, len(message))