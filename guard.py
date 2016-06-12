import sys
from gui import MainWidget
from encoder import Encoder
from utils import write, read


class Guard:

    def __init__(self):
        self.data_directory = "data"
        self.gui = MainWidget(self)

    @staticmethod
    def format(entries):
        string = ""
        for entry in entries:
            string += (entry + ':' + entries[entry] + '\n\r')
        return string

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
        write(cipher, filename, self.data_directory, self.gui.log_message)

    def read(self, passphrase, filename):
        cipher = read(filename, self.data_directory, self.gui.log_message)
        return Encoder.decode(passphrase, self.salt(), cipher)

    @staticmethod
    def salt():
        return 'thisIsMadness'

guard = Guard()
guard.gui.run()