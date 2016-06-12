import sys
from gui import MainWidget
from encoder import Encoder
from datastore import DataStore

class Guard:

    def __init__(self):
        self.gui = MainWidget(self)
        self.data_store = DataStore("data", self.gui.log_message)

    @staticmethod
    def format(entries):
        string = ""
        for entry in entries:
            string += (entry + ':' + entries[entry] + '\n\r')
        return string

    def entry_exists(self, file):
        if file in self.data_store.get_entries():
            self.gui.log_message("Entry " + file + " already exists.")
            return True
        return False

    def save(self, entries, passphrase):
        string = self.format(entries)
        filename = entries["Entry-Name"]
        if filename == "":
            self.gui.log_message("Entry-Name need to be set")
            return
        if passphrase == "":
            self.gui.log_message("Passphrase need to be set")
            return
        cipher = Encoder.encode(passphrase, self.salt(), string)
        self.data_store.write(cipher, filename)

    def read(self, passphrase, filename):
        cipher = self.data_store.read(filename)
        return Encoder.decode(passphrase, self.salt(), cipher)

    def get_entries(self):
        return self.data_store.get_entries()

    @staticmethod
    def salt():
        return 'thisIsMadness'

guard = Guard()
guard.gui.run()