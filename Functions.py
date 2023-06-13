import tkinter as tk

def Click(self, text):
    if text == "=":
        #Evaluate the expression and display the result
        try:
            result = eval(self.input_field.get())
            self.input_field.delete(0, tk.END)
            self.input_field.insert(tk.END, str(result))
        except:
            self.input_field.delete(0, tk.END)
            self.input_field.insert(tk.END, "Error")
    elif text == "C":
        self.input_field.delete(0, tk.END)
    else:
        # Append the button text to the entry widget
        self.input_field.insert(tk.END, text)
