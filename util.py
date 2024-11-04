def new_alph(ch):
    ch = ch.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph
    
   
def encrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = big_key[i].lower()
            shift = alph.index(key_char)
            if char.islower():
                res += alph[(alph.index(char) + shift) % 26]
            else:
                res += alph[(alph.index(char.lower()) + shift) % 26].upper()
        else:
            res += char
    return res

    
def decrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = big_key[i].lower()
            shift = alph.index(key_char)
            if char.islower():
                res += alph[(alph.index(char) - shift) % 26]
            else:
                res += alph[(alph.index(char.lower()) - shift) % 26].upper()
        else:
            res += char
    return res
