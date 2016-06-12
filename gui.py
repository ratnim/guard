import tkinter as tk
from tkinter import messagebox


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

    def _create_passphrase_entry(self, row):
        self.passphrase_hide = tk.IntVar()
        tk.Label(self.work_frame, text="Passphrase").grid(row=row)
        self.passphrase_entry = tk.Entry(self.work_frame, show="*")
        self.passphrase_entry.grid(row=row, column=1)
        t = tk.Checkbutton(self.work_frame,
                       text="Hide",
                       variable=self.passphrase_hide,
                       command=self._toggle_passphrase)
        t.grid(row=row, column=2)
        t.select()

    def _toggle_passphrase(self):
        if self.passphrase_hide.get():
            self.passphrase_entry.config(show="*")
        else:
            self.passphrase_entry.config(show="")


class NewEntryWidget(WorkingWidget):
    """Widget to create a new entry"""

    def __init__(self, parent, worker):
        super(NewEntryWidget, self).__init__(parent, worker)

        self.worker = worker
        self.entries = {}
        self.row = 0

        self._create_passphrase_entry(self._next_row())

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

    def _save_pressed(self):
        values = {}
        entry_name = self.entries["Entry-Name"].get()
        for entry in self.entries:
            values[entry] = self.entries[entry].get()
        if self.worker.entry_exists(entry_name):
            if not tk.messagebox.askokcancel("Overwrite", "Entry " + entry_name + " already exists. Overwrite?"):
                return
        self.worker.save(values, self.passphrase_entry.get())


class OpenEntryWidget(WorkingWidget):
    """Widget to create a new entry"""

    def __init__(self, parent, worker):
        super(OpenEntryWidget, self).__init__(parent, worker)

        self.worker = worker
        self._create_passphrase_entry(0)

        tk.Button(self.button_frame, text='Open', width=25, command=self._open_pressed).pack(
            side=tk.LEFT)

        self._show_entries()

    def _selected_entries(self):
        entries = []
        for entry in self.entries:
            if self.enable[entry].get():
                entries.append(entry)
        return entries

    def _show_entries(self):
        self.entries = self.worker.get_entries()
        self.enable = {}
        row = 1;
        column = 0;
        max_row = len(self.entries) / 3
        for entry in self.entries:
            self.enable[entry] = tk.IntVar()
            t = tk.Checkbutton(self.work_frame, text=entry, variable=self.enable[entry])
            t.grid(row=row, column=column)
            t.deselect()
            row += 1
            if max_row + 1 <= row:
                row = 1
                column += 1

    def _open_pressed(self):
        files = self._selected_entries()
        passphrase = self.passphrase_entry.get()
        for file in files:
            content = self.worker.read(passphrase, file)
            self._open_output_widget(file, content)

    def _open_output_widget(self, name, content):
        widget = tk.Tk()
        widget.title("Entry : " + name)
        text = tk.Text(widget ,height=10, width=40)
        scroll_bar = tk.Scrollbar(widget)
        text.pack(side=tk.LEFT, fill=tk.Y)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_bar.config(command=text.yview)
        text.config(yscrollcommand=scroll_bar.set)
        text.insert(tk.END, content)
        text.configure(bg=widget.cget('bg'), relief=tk.FLAT)
        text.configure(state="disabled")

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
        file_menu.add_command(label="Add", command=self._new_entry)
        file_menu.add_command(label="Open", command=self._open_entry)

    def _get_working_frame(self, widget_class=WorkingWidget, worker=None):
        if not self.working_widget is None:
            self.working_widget.destroy()
        self.working_widget = widget_class(self.frame, worker)
        self.working_widget.frame.pack(side=tk.TOP)

    def _new_entry(self):
        self.log_message("Select new entry widget.")
        self._get_working_frame(NewEntryWidget, self.worker)

    def _open_entry(self):
        self.log_message("Select open entry widget.")
        self._get_working_frame(OpenEntryWidget, self.worker)

    def log_message(self, message):
        print(message)
        self.log.configure(state="normal")
        self.log.insert(tk.END, message + "\r\n")
        self.log.configure(state="disabled")
        self.log.see(tk.END)

    def run(self):
        tk.mainloop()