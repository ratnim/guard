import sys
from gui import MainWidget
from encoder import Encoder
from utils import write, read

class Guard:
    def __init__(self):
        if len(sys.argv) == 1:
            self.open_gui();

    def format(self, entries):
        string = ""
        for entry in entries:
            string += (entry + ':' + entries[entry] + '\n\r')
        return string

    def save(self, entries, passphrase):
        string = self.format(entries)
        filename = entries["Entry-Name"]
        if filename == "":
            print("Entry-Name need to be set")
            return
        if passphrase == "":
            print("Passphrase need to be set")
            return
        cipher = Encoder.encode(passphrase, self.salt(), string)
        write(cipher, filename)

    def read(self, passphrase, filename):
        cipher = read(filename)
        print(cipher)
        return Encoder.decode(passphrase, self.salt(), cipher)

    def open_gui(self):
        widget = MainWidget(self.save, self.read)
        widget.open()

    def salt(self):
        return 'thisIsMadness'
Guard()