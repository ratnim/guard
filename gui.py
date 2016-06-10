import tkinter as tk

class MainWidget:
    """"Main GUI element"""

    def __init__(self, save):
        self.tk_master = tk.Tk()
        self.tk_master.title("Guard")
        self.save_callback = save
        self.entries = {}
        self.row = 0
        self.passphrase = None

    def open(self):
        self.passphrase = self.generate_entry("Passphrase", False)
        self.generate_entry("Entry-Name")
        self.generate_entry("Company")
        self.generate_entry("Url")
        self.generate_entry("E-Mail")
        self.generate_entry("Login-Name")
        self.generate_entry("Password")

        row = self.next_row()

        tk.Button(self.tk_master, text='Close', width=25, command=self.tk_master.destroy).grid(row=row, column=0, sticky=tk.W, pady=4)
        tk.Button(self.tk_master, text='Save', width=25, command=self.save_pressed).grid(row=row, column=1, sticky=tk.W, pady=4)

        tk.mainloop()

    def save_pressed(self):
        values = {}

        for entry in self.entries:
            values[entry] = self.entries[entry].get()
        self.save_callback(values, self.passphrase.get())

    def generate_entry(self, name, is_content=True):
        row = self.next_row()
        tk.Label(self.tk_master, text=name).grid(row=row)
        entry = tk.Entry(self.tk_master)
        entry.grid(row=row, column=1)
        if is_content:
            self.entries[name] = entry
        return entry

    def next_row(self):
        self.row += 1
        return self.row