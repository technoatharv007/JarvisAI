import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="write a letter for birthday to friend ",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)