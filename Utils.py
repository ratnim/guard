# Shared helper functions


# Extends string until it is a multiple of base
def extend_string_to_base(string, base):
    fit = len(string) % base
    if fit == 0:
        return string
    for i in range(base - fit):
        string += ' '
        return string


def write(content, filename):
    print("write file " + filename)
    file = open(filename, 'wb')
    file.write(content)


def read(filename):
    print("Read file " + filename)
    file = open(filename, 'rb')
    return file.read()
