import tkinter as tk
import Constant as cons
from Functions import *

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("312x324")
        self.resizable(0, 0)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_input_field()
        self.create_buttons()

    def create_input_field(self):
        input_frame = tk.Frame(
            width=312,
            height=50,
            bd=0,
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=2,
        )
        input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(
            input_frame,
            font=("arial", 18, "bold"),
            textvariable=self.input_text,
            width=50,
            bg="#eee",
            bd=0,
            justify=tk.RIGHT,
        )
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

    def create_buttons(self):
        buttons_frame = tk.Frame(width=312, height=272.5, bg="grey")
        buttons_frame.pack()
        
        for data in cons.buttons:
            text, row, col, colspan, width = data
            button = tk.Button(
                buttons_frame,
                text=text,
                fg="black",
                width=width,
                height=3,
                bd=0,
                bg="#fff",
                cursor="hand2"
            )
            button.grid(row=row, column=col, columnspan=colspan, padx=1, pady=1)
            button.config(command=lambda text=text: Click(self, text))