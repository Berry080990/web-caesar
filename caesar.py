import string

def encrypt(text, rot):
    crypt = ""
    for i in text:
        crypt = crypt + rotate_character(i, rot)
    return crypt

def alphabet_position(letter):
    if letter.isupper():
        return string.ascii_uppercase.index(letter)
    else:
        return string.ascii_lowercase.index(letter)

def rotate_character(char, rot):
    if char.isupper():
        position = alphabet_position(char)
        new = ((position + rot) % 26) + 65
        return chr(new)
    elif char.islower():
        position = alphabet_position(char)
        new = ((position + rot) % 26) + 97
        return chr(new)
    else:
        return char
