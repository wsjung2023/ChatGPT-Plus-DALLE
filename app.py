import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

###models = dict(openai.Model.list())   ###모델들 찍어내기
### for i in models['data']:
###    if i['id'].startswith('gpt'):
###        print(i['id'])'''

st.title("Wooseub's Test WEBAPP ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt") 
    size = st.selectbox("Size", ["1024x1024", "512x512","256x256"], )
    submit = st.form_submit_button("Submit")
    ###모델들 찍어내기 st.write(models)

### GPT 프론프트변수에 GPT에게 내릴 프롬프트를 만들고
### 시스템 역할과 내용을 지정 해준다 GPT에게 명령을 내려놓음
if submit and user_input:
    gpt_promt = [{
            "role": "system",
            "content": "Imagine the detail appearence of the input. Response it shortly around 50 words."
    }]

    gpt_promt.append({    
            "role": "user",
            "content": user_input        
    })

### 스피너 만들기
    with st.spinner("Waiting for ChatGPT..."):      
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_promt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)
### DALLE 에게 명령하기 
### 스피너 만들기
    with st.spinner("Waiting for DALL-E..."):      
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size
        )

    st.image(dalle_response["data"][0]["url"])

    ### 이제 시작
    ### Streamlit Cloud 
    ### https://share.streamlit.io