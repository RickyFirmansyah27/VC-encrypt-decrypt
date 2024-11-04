from pycipher import Vigenere

def encrypt(text, key):
    # Menggunakan fungsi encrypt dari Vigenere
    cipher = Vigenere(key)
    return cipher.encipher(text)

def decrypt(text, key):
    # Menggunakan fungsi decrypt dari Vigenere
    cipher = Vigenere(key)
    return cipher.decipher(text)
