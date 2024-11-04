import streamlit as st
import util

def main(pesan, key, mode, cipher_type, shift=0):
    if cipher_type == "Caesar":
        if mode == "Encrypt":
            result = util.caesar_encrypt(pesan, shift)
            st.header('#======== Start Encrypt (Caesar) =======#') 
            st.write('Encryption Text       : ' + result)
        
        elif mode == "Decrypt":
            result = util.caesar_decrypt(pesan, shift)
            st.header('#======== Start Decrypt (Caesar) =======#')
            st.write('Decryption Text       : ' + result)
            
    elif cipher_type == "Vigenere":
        if len(key) <= len(pesan):
            big_key = (key * (len(pesan) // len(key))) + key[:len(pesan) % len(key)]
            if mode == "Encrypt":
                result = util.vigenere_encrypt(pesan, big_key)
                st.header('#======== Start Encrypt (Vigenere) =======#') 
                st.write('Encryption Text       : ' + result)
            
            elif mode == "Decrypt":
                result = util.vigenere_decrypt(pesan, big_key)
                st.header('#======== Start Decrypt (Vigenere) =======#')
                st.write('Decryption Text       : ' + result)
        else:
            st.write('Error: len(key) > len(text)')
               
if __name__ == '__main__':
    st.title("Program Encryption and Decryption with Ciphers")
    
    # Sidebar untuk memilih cipher type dan mode
    cipher_type = st.sidebar.selectbox("Choose Cipher Type", ("Caesar", "Vigenere"))
    mode = st.sidebar.radio("Choose Mode", ("Encrypt", "Decrypt"))
    
    form = st.form(key='my-form')
    pesan = form.text_input('Silakan Masukan Text Anda', '-')
    
    if cipher_type == "Caesar":
        shift = form.number_input('Masukan Shift (untuk Caesar)', min_value=0, max_value=25, value=0)
        key = None  # No key needed for Caesar
    else:
        key = form.text_input('Silakan Masukan Key Anda', '-')
        shift = None  # No shift needed for Vigenere

    submit = form.form_submit_button('Generate')
   
    if submit:
        main(pesan, key, mode, cipher_type, shift)
