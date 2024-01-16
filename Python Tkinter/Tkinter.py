# Date : 26/11/2023
# Assignment: Unit Conversion Tool
# Author : Sumit Sohal
# Student id : C0902846
import tkinter as tk
from tkinter import ttk

class TemperatureConverterApp:
    def _init_(self, tree):
        self.tree = tree
        self.tree.title("Temperature Conversion Tool")

        # Variables for user input and result
        self.user_input = tk.DoubleVar()
        self.results = tk.StringVar()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame for user input
        input_frm = ttk.Frame(self.tree, padding="10")
        input_frm.grid(row=0, column=0)

        ttk.Label(input_frm, text="Enter Value in Celsius:").grid(row=0, column=0)
        entry_input = ttk.Entry(input_frm, textvariable=self.user_input)
        entry_input.grid(row=0, column=1)

        # Frame for result display
        result_frame = ttk.Frame(self.tree, padding="10")
        result_frame.grid(row=1, column=0)

        ttk.Label(result_frame, text="Result in Fahrenheit:").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(result_frame, textvariable=self.results).grid(row=0, column=1)

        # Button to perform the conversion
        convert_button = ttk.Button(self.tree, text="Convert", command=self.convert)
        convert_button.grid(row=2, column=0, pady=10)

    def convert(self):
        # Conversion logic from Celsius to Fahrenheit
        try:
            celsius = float(self.user_input.get())
            fahrenheit = (celsius * 9/5) + 32
            self.results.set(round(fahrenheit, 2))
        except ValueError:
            self.results.set("Invalid Input")

if __name__ == "__main__":
    tree = tk.Tk()
    app = TemperatureConverterApp(tree)
    tree.mainloop()