import pyperclip


def set_copy(msg):
    pyperclip.copy(msg)


def get_copy():
    return pyperclip.paste()
