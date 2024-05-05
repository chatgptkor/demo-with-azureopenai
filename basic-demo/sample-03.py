import openai
import streamlit as st

openai.api_key = ''
openai.azure_endpoint=''
openai.api_type = 'azure'
openai.api_version = '2023-05-15'

st.header("welcome to AIChatBot", divider='rainbow')
st.write('안녕하세요. 반갑습니다. 만물박사 챗봇 입니다')

subject=st.text_input('시의 주제를 말씀해주세요.')
st.write('주제는'+subject)
content=st.text_area('시의 내용에 대해 말해주세요.')

btn_click=st.button('답변')

if(btn_click):
    with st.spinner('please wait .....'):
        result = openai.chat.completions.create(
            model='demo-gpt35t1106',
            temperature=1,
            messages=[
                {"role": "system", "content": "You are an AI assistant that helps people find information."},
                {"role": "user", "content": '시의 주제는 '+subject},
                {"role": "user", "content": '시의 내용은 '+content},
                {"role": "user", "content": '이 내용으로 시를 지어줘'}
            ]
        )
    st.success('done!')

    st.write(result.choices[0].message.content)
