import sv_ttk as sun_valley

from tkinter.ttk import (
    Frame,
    Entry,
    Button
)

from tkinter import Tk, PhotoImage


chars = [
    '^', '(', ')', 'C',
    '7', '8', '9', '<',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


class Gui(Tk):
    def __init__(self, title: str):
        super().__init__()

        self.geometry('312x436')
        self.resizable(0, 0)
        self.title(title)

        sun_valley.set_theme('light')
        self.buttons = []

        self.load_entry()
        self.load_buttons()

        self.iconphoto(False, PhotoImage(file='./calculator/assets/icon_small.png'))


    def load_entry(self):
        frame_entry = Frame(self).grid()

        self.entry = Entry(
            master=frame_entry,
            justify='center',
            width=37,
        )

        self.entry.grid(row=0, columnspan=4, padx=(18, 0), pady=(20, 5), ipady=8)


    def load_buttons(self):
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
        

    def set_button_command(self, index):
        self.buttons[index]['command'] = lambda: self.on_button_clicked(chars[index])


    def on_button_clicked(self, button):
        entry_length = len(self.entry.get())

        match button:
            case 'C':
                if entry_length >= 1:
                    self.entry.delete(0, entry_length)

            case '<':
                if entry_length >= 1:
                    self.entry.delete(entry_length - 1)

            case '=':
                self.on_button_clicked('C')

            case _:
                self.entry.insert(entry_length, button)