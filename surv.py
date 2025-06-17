import streamlit as st
import pandas as pd
import uuid
if 'user_data' not in st.session_state:
    st.session_state.user_data= []
def user_data(name,age,email,gender,phoneno,country,city,occupation,hobby,add):
    unique_id = uuid.uuid4()
    user = {
        'User_ID': unique_id,
        'Name' : name,
        'Age' : age,
        'Email': email,
        'Gender': gender,
        'Phone_No': phoneno,
        'Country': country,
        'City': city,
        'Occupation':occupation,
        'Hobbies':hobby,
        'Notes':add
    }
    st.session_state.user_data.append(user)

st.header('User Information form')
with st.form(key='My_Form'):
    name=st.text_input('What is your Name')
    age = st.text_input('What is your age')
    email=st.text_input('Enter your email')
    gender=st.radio('Select your gender: ', ['Male','Female'])
    phoneno=st.text_input("Enter your Phone no")
    country=st.text_input("Enter your country")
    city=st.text_input("Enter your city")
    occupation=st.text_input("Enter your occupation")
    hobby=st.text_input("Enter your hobbies")
    add=st.text_input("Enter any additional notes")

    sub_button=st.form_submit_button(label='Submit')

if sub_button:
    if name.strip() and email.strip() and '@' in email:
        user_data(name,age,email,gender,phoneno,country,city,occupation,hobby,add)
        st.success('User data submitted')
    else:
        st.error("No data given")

if st.session_state['user_data']:
    st.subheader("Submitted users")
    df=pd.DataFrame(st.session_state['user_data'])
    st.dataframe(df,use_container_width=True)
    csv = df.to_csv(index=False)
    st.download_button( 
        label='download file',
        data=csv,
        file_name='user_data.csv',
        mime='text/csv'
    )