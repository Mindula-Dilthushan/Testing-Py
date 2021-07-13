# Alpha X Software Company
# Mindula Dilthushan
# 21-07-13
# Module 01 - Text Change Py UI

import tkinter as tk
from tkinter import ttk

class ChangeName(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World")

        name_label = ttk.Label(self, text="Input Your Name : ")
        name_entry = ttk.Entry(self, textvariable=self.name)
        ch_button = ttk.Button(self, text=" Change ", command=self.on_change)
        hello_label = ttk.Label(self, textvariable=self.hello_string,
                                font=("TkDefaultFont", 14), wraplength=500)

        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)
        self.columnconfigure(1, weight=1)

    def on_change(self):

        if self.name.get().strip():
            self.hello_string.set("Hello " + self.name.get())
        else:
            self.hello_string.set("Hello World")


class MyApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Change Name")
        self.geometry("400x200")
        self.resizable(width=False, height=False)


        ChangeName(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
