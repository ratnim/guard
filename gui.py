import tkinter as tk


class WorkingWidget:
    """Basic working widget"""

    def __init__(self, parent, worker=None):
        self.frame = tk.Frame(parent)
        self.work_frame = tk.Frame(self.frame)
        self.work_frame.pack(side=tk.TOP)
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(side=tk.BOTTOM)

    def destroy(self):
        self.frame.destroy()


class NewEntryWidget(WorkingWidget):
    """Widget to create a new entry"""

    def __init__(self, parent, worker):
        super(NewEntryWidget, self).__init__(parent, worker)

        self.entries = {}
        self.row = 0
        self.passphrase_hide = tk.IntVar()
        self.passphrase_entry = None
        self.worker = worker

        self.passphrase_entry = self.generate_entry("Passphrase", False)
        tk.Checkbutton(self.work_frame,
                       text="Hide",
                       variable=self.passphrase_hide,
                       command=self.toggle_passphrase).grid(row=self.row, column=2)

        self.generate_entry("Entry-Name")
        self.generate_entry("Company")
        self.generate_entry("Url")
        self.generate_entry("E-Mail")
        self.generate_entry("Login-Name")
        self.generate_entry("Password")

        tk.Button(self.button_frame, text='Save', width=25, command=self._save_pressed).pack(side=tk.LEFT)

    def generate_entry(self, name, is_content=True):
        tk.Label(self.work_frame, text=name).grid(row=self._next_row())
        entry = tk.Entry(self.work_frame)
        entry.grid(row=self.row, column=1)
        if is_content:
            self.entries[name] = entry
        return entry

    def _next_row(self):
        self.row += 1
        return self.row

    def toggle_passphrase(self):
        if self.passphrase_hide.get():
            self.passphrase_entry.config(show="*")
        else:
            self.passphrase_entry.config(show="")

    def _save_pressed(self):
        values = {}
        for entry in self.entries:
            values[entry] = self.entries[entry].get()
        self.worker.save(values, self.passphrase_entry.get())


class MainWidget:
    """"Main GUI element"""

    def __init__(self, worker):
        self.tk_master = tk.Tk()
        self.tk_master.title("Guard")
        self.worker = worker

        self.frame = tk.Frame(self.tk_master)
        self.frame.pack()

        self.working_widget = None

        self.log_frame = tk.Frame(self.frame)
        self.log_frame.pack(side=tk.BOTTOM)

        self._setup_log()
        self._setup_menu()

    def _setup_log(self):
        self.log = tk.Text(self.log_frame, width=60, height=4)
        self.log.configure(bg=self.log_frame.cget('bg'))
        self.log.config(bg="sky blue")
        self.log.configure(state="disabled")
        self.log.grid(row=0, column=0, rowspan=4, columnspan=3)
        self.log_message("Guard, Version 1.0")

    def _setup_menu(self):
        menu = tk.Menu(self.frame)
        self.tk_master.config(menu=menu)
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Entry", command=self._new_entry)
        file_menu.add_command(label="Open", command=self._open_entry)

    def _get_working_frame(self, widget_class=WorkingWidget, worker=None):
        if not self.working_widget is None:
            self.working_widget.destroy()
        self.working_widget = widget_class(self.frame, worker)
        self.working_widget.frame.pack(side=tk.TOP)

    def _new_entry(self):
        self.log_message("Open new entry.")

        self._get_working_frame(NewEntryWidget, self.worker)

    def _open_entry(self):
        self._get_working_frame()

        tk.Button(self.working_widget.button_frame, text='Open', width=25, command=self._open_pressed).pack(side=tk.LEFT)

    def log_message(self, message):
        print(message)
        self.log.configure(state="normal")
        self.log.insert(tk.END, message + "\r\n")
        self.log.configure(state="disabled")
        self.log.see(tk.END)

    def _open_pressed(self):
        filename = self.entries["Entry-Name"].get()
        passphrase = self.passphrase_entry.get()
        widget = tk.Tk()
        widget.title("Entry : " + filename)
        content = self.worker.read(passphrase, filename)
        text = tk.Text(widget ,height=10, width=40)
        scroll_bar = tk.Scrollbar(widget)
        text.pack(side=tk.LEFT, fill=tk.Y)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_bar.config(command=text.yview)
        text.config(yscrollcommand=scroll_bar.set)
        text.insert(tk.END, content)
        text.configure(bg=widget.cget('bg'), relief=tk.FLAT)
        text.configure(state="disabled")

    def run(self):
        tk.mainloop()