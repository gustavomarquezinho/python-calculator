import sv_ttk as sun_valley
from .calcs import Calcs

from tkinter.ttk import (
    Label,
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

columns = 4


class Gui(Tk):
    def __init__(self, title: str):
        super().__init__()

        self.center_window(312, 472)
        self.resizable(0, 0)
        self.title(title)

        sun_valley.set_theme('light')
        self.buttons = []

        self.create_preview()
        self.create_entry()
        self.create_buttons()

        self.iconphoto(False, PhotoImage(file='./calculator/icon_small.png'))


    def center_window(self, size_x: int, size_y: int) -> None:
        pos_x = (self.winfo_screenwidth() / 2) - (size_x / 2)
        pos_y = (self.winfo_screenheight() / 2) - (size_y / 2)

        self.geometry('{}x{}+{}+{}' .format(size_x, size_y, int(pos_x), int(pos_y)))


    def create_preview(self) -> None:
        self.preview = Label(master=self)

        self.preview.grid(
            column=0, row=0,
            columnspan=columns,
            padx=(0, 15),
            pady=(10, 5),
            sticky='e'
        )


    def create_entry(self) -> None:
        self.entry = Entry(master=self, justify='center', width=36)

        self.entry.grid(
            column=0, row=1,
            columnspan=columns,
            padx=(15, 0), 
            pady=(0, 15),
            ipady=10
        )

        self.entry.bind('<Return>', lambda bind: self.on_button_clicked('='))


    def create_buttons(self) -> None:
        col, row = 0, 2

        for index, char in enumerate(chars):
            padx = (18, 2) if col == 0 else (2, 2)
 
            self.buttons.append(
                Button(master=self, text=char, width=6)
            )

            self.buttons[len(self.buttons) - 1].grid(
                column=col,
                row=row,
                padx=padx,
                pady=2,
                ipady=16
            )

            if (index + 1) % columns != 0:
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

                elif len(self.preview['text']) >= 1:
                    self.preview['text'] = ''

            case '<':
                if entry_length >= 1:
                    self.entry.delete(entry_length - 1)

            case '=':
                calcs = Calcs(self.entry.get())
                self.on_button_clicked('C')

                if calcs.error is not None:
                    self.preview['text'] = calcs.error
                    return

                self.entry.insert(0, calcs.get_formatted())
                self.preview['text'] = calcs.operation_copy

            case _:
                self.entry.insert(entry_length, button)
