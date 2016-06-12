# Shared helper functions
import os


class DataStore:
    """simple Filesytem storage class"""

    def __init__(self, path, log_callback=print):
        self.directory = path
        self.log = log_callback
        if not os.path.exists(path):
            os.makedirs(path)

    def write(self, content, filename):
        filePath = os.path.sep.join([ self.directory, filename ])
        self.log("Write file: " + filePath)
        file = open( filePath, 'wb')
        file.write(content)

    def read(self, filename):
        filePath = os.path.sep.join([self.directory, filename])
        self.log("Read file: " + filePath)
        file = open(filePath, 'rb')
        return file.read()

    def get_entries(self):
        entries = []
        for filename in os.listdir(self.directory):
            entries.append(filename)
        return entries