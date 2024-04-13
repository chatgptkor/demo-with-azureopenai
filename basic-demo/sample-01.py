import openai

openai.api_key = ''
openai.azure_endpoint=''
openai.api_type = 'azure'
openai.api_version = '2023-05-15'

query = input('궁금한 걸 물어보세요?')
result = openai.chat.completions.create(
    model='demo-gpt35t1106',
    temperature=1,
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": query+"가 뭐야?"}
    ]

)

generated_text = result.choices[0].message.content