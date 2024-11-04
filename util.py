from pycipher import Vigenere

def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) + shift_amount
            if char.islower():
                result += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
            else:
                result += chr(shifted) if shifted <= ord('Z') else chr(shifted - 26)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    cipher = Vigenere(key)
    return cipher.encipher(text)

def vigenere_decrypt(text, key):
    cipher = Vigenere(key)
    return cipher.decipher(text)
