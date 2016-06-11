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
        self.log = None

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

        self.log = tk.Text(self.tk_master, width=60, height=4)
        self.log.configure(bg=self.tk_master.cget('bg'))
        self.log.config(bg="sky blue")
        self.log.configure(state="disabled")
        self.log.grid(row=self.next_row(), column=0, rowspan=4, columnspan=3)
        self.row += 4
        self.log_message("Guard, Version 1.0")


        tk.mainloop()

    def log_message(self, message):
        print(message)
        self.log.configure(state="normal")
        self.log.insert(tk.END, message + "\r\n")
        self.log.configure(state="disabled")
        self.log.see(tk.END)

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
        widget.title("Entry : " + filename)
        content = self.read_callback(passphrase, filename)
        text = tk.Text(widget ,height=10, width=40)
        scroll_bar = tk.Scrollbar(widget)
        text.pack(side=tk.LEFT, fill=tk.Y)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_bar.config(command=text.yview)
        text.config(yscrollcommand=scroll_bar.set)
        text.insert(tk.END, content)
        text.configure(bg=widget.cget('bg'), relief=tk.FLAT)
        text.configure(state="disabled")