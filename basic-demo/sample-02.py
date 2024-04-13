import openai
import streamlit as st

openai.api_key = ''
openai.azure_endpoint=''
openai.api_type = 'azure'
openai.api_version = '2023-05-15'

st.header("welcome to AIChatBot", divider='rainbow')
st.write('안녕하세요. 반갑습니다. 만물박사 챗봇 입니다')

query=st.text_input('궁금한 내용을 입력하세요.')
btn_click=st.button('답변')

if(btn_click):
    result = openai.chat.completions.create(
        model='demo-gpt35t1106',
        temperature=1,
        messages=[
            {"role": "system", "content": "You are an AI assistant that helps people find information."},
            {"role": "user", "content": query+"가 뭐야?"}
        ]
    )
    st.write(result.choices[0].message.content)