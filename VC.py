import streamlit as st
import util

def main(pesan, key, mode):
    # Memastikan kunci sama panjang atau lebih panjang dari pesan
    if len(key) <= len(pesan):
        # Memperluas kunci menjadi ukuran yang sama dengan pesan
        big_key = (key * (len(pesan) // len(key))) + key[:len(pesan) % len(key)]
        
        if mode == "Encrypt":
            text_result = util.encrypt(pesan, big_key)
            st.header('#======== Start Encrypt =======#') 
            st.write('Encryption Text       : ' + text_result)
        
        elif mode == "Decrypt":
            text_result = util.decrypt(pesan, big_key)
            st.header('#======== Start Decrypt =======#')
            st.write('Decryption Text       : ' + text_result)
            
    else:
        st.write('Error: len(key) > len(text)')
               
if __name__ == '__main__':
    st.title("Program Encryption and Decryption Vigenere Cipher")
    
    # Sidebar untuk memilih mode
    mode = st.sidebar.radio("Choose Mode", ("Encrypt", "Decrypt"))
    
    form = st.form(key='my-form')
    pesan = form.text_input('Silakan Masukan Text Anda', '-')
    key = form.text_input('Silakan Masukan Key Anda', '-')
    submit = form.form_submit_button('Generate')
   
    if submit:
        main(pesan, key, mode)
