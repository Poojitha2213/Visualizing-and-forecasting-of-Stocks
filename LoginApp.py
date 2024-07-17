# # Authentication
import streamlit as st


st.title('Login Page')

user_name=st.text_input('Enter Your Username : ')
user_password=st.text_input('Enter Your Password : ')


st.write(f'''
    <a target="_self" href="http://localhost:8501/">
        <button style="background-color:transparent; border-radius: 10px; padding: 5px 10px; border: solid 1px white">
            Login
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)



