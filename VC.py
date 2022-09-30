import streamlit as st
import util

def main():
        
    if len(key) <= len(pesan):
        big_key = key * (len(pesan) // len(key)) + key[:len(pesan) % len(key)]
        text_encrypt = util.encrypt(pesan, big_key)
        text_decrypt = util.decrypt(text_encrypt, big_key)
        
        st.header('#========Start Encrypt=======#') 
        st.write('Encryption Text       : ' + text_encrypt)
       
        st.header('#========Start Decrypt=======#')
        st.write('Descryption Text      : ' + text_decrypt)
        
    else:
        st.write('Error: len(key)>len(text) ')
               

        
     
    
if __name__ == '__main__':
    st.title("Program Encyption and Decryption Vigenere Chiper")
    form = st.form(key='my-form')
    pesan = form.text_input('Silakan Masukan Text Anda)', '-')
    key = form.text_input('Silakan Masukan Key Anda)', '-')
    submit = form.form_submit_button('Generate')
    
   
    if submit:
        main()
       
                        
    
     
