import tkinter as tk

class MainWidget:
    """"Main GUI element"""

    def __init__(self):
        self.tk_master = tk.Tk()
        self.tk_master.title("Guard")

    def open(self):
        self.generate_entry("Company", 0)
        self.generate_entry("Url", 1)
        self.generate_entry("E-Mail", 2)
        self.generate_entry("Login-Name", 3)
        self.generate_entry("Password", 4)

        tk.Button(self.tk_master, text='Close', width=25, command=self.tk_master.destroy).grid(row=5, column=0, sticky=tk.W, pady=4)
        tk.Button(self.tk_master, text='Save', width=25, command=self.tk_master.destroy).grid(row=5, column=1, sticky=tk.W, pady=4)

        tk.mainloop()

    def generate_entry(self, name, row):
        tk.Label(self.tk_master, text=name).grid(row=row)
        tk.Entry(self.tk_master).grid(row=row, column=1)