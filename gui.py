import tkinter as tk


class MainWidget:
    """"Main GUI element"""

    def __init__(self, save, read):
        self.tk_master = tk.Tk()
        self.tk_master.title("Guard")
        self.save_callback = save
        self.read_callback = read
        self.entries = {}
        self.row = 0
        self.passphrase = {}
        self.passphrase_hide = tk.IntVar()
        self.passphrase_entry = None

    def open(self):
        self.passphrase_entry = self.generate_entry("Passphrase", False)
        tk.Checkbutton(self.tk_master,
                       text="Hide",
                       variable=self.passphrase_hide,
                       command=self.toggle_passphrase).grid(row=self.row, column=2)

        self.generate_entry("Entry-Name")
        self.generate_entry("Company")
        self.generate_entry("Url")
        self.generate_entry("E-Mail")
        self.generate_entry("Login-Name")
        self.generate_entry("Password")

        row = self.next_row()

        tk.Button(self.tk_master, text='Close', width=25, command=self.tk_master.destroy).grid(row=row, column=0, sticky=tk.W, pady=4)
        tk.Button(self.tk_master, text='Save', width=25, command=self.save_pressed).grid(row=row, column=1, sticky=tk.W, pady=4)
        tk.Button(self.tk_master, text='Open', width=25, command=self.open_pressed).grid(row=row, column=2, sticky=tk.W, pady=4)
        tk.mainloop()

    def toggle_passphrase(self):
        if self.passphrase_hide.get():
            self.passphrase_entry.config(show="*")
        else:
            self.passphrase_entry.config(show="")

    def save_pressed(self):
        values = {}

        for entry in self.entries:
            values[entry] = self.entries[entry].get()
        self.save_callback(values, self.passphrase_entry.get())

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

    def open_pressed(self):
        filename = self.entries["Entry-Name"].get()
        passphrase = self.passphrase_entry.get()
        widget = tk.Tk()
        widget.title(filename)
        text = tk.Text(widget ,height=len(self.entries),width=30)
        text.grid(row=0)
        content = self.read_callback(passphrase, filename)
        text.insert(tk.END, content)