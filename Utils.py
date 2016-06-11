# Shared helper functions
import os

# Extends string until it is a multiple of base
def extent_string_to_base(string, base):
    while len(string) % base:
        string += ' '
    return string


def write(content,filename, path=""):
    filePath = os.path.sep.join([ path, filename ])
    if not os.path.exists(path):
        os.makedirs(path)
    print("write file " + filePath)
    file = open( filePath, 'wb')
    file.write(content)


def read(filename, path=""):
    filePath = os.path.sep.join([path, filename])
    print("Read file " + filePath)
    file = open(filePath, 'rb')
    return file.read()
