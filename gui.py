import tkinter as tk

class MainWidget:
    """"Main GUI element"""

    def __init__(self, save):
        self.tk_master = tk.Tk()
        self.tk_master.title("Guard")
        self.save_callback = save
        self.entries = {}

    def open(self):
        self.generate_entry("Entry-Name")
        self.generate_entry("Company")
        self.generate_entry("Url")
        self.generate_entry("E-Mail")
        self.generate_entry("Login-Name")
        self.generate_entry("Password")

        tk.Button(self.tk_master, text='Close', width=25, command=self.tk_master.destroy).grid(row=len(self.entries), column=0, sticky=tk.W, pady=4)
        tk.Button(self.tk_master, text='Save', width=25, command=self.save_pressed).grid(row=len(self.entries), column=1, sticky=tk.W, pady=4)

        tk.mainloop()

    def save_pressed(self):
        values = {}
        for entry in self.entries:
            values[entry] = self.entries[entry].get()
        self.save_callback(values)

    def generate_entry(self, name):
        tk.Label(self.tk_master, text=name).grid(row=len(self.entries))
        entry = tk.Entry(self.tk_master)
        entry.grid(row=len(self.entries), column=1)
        self.entries[name] = entry