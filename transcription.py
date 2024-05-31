#! /home/frijol/Desktop/no_recollection/venv/bin python

import base64
import os
from openai import OpenAI
from dotenv import load_dotenv

image_path = "/home/frijol/Desktop/no_recollection/scans/tmp/scan.png"
base_prompt_file = "/home/frijol/Desktop/no_recollection/base_prompt.txt"
image_question = "qu'est-ce qu'il y a dans cette image ? Merci d'indiquer seulement la partie manuscrite, sans indiquer que c'est la partie manuscrite, juste le texte"

load_dotenv()

client = OpenAI(api_key=os.getenv("GPT_KEY"))

# List available models

# models = client.models.list()
# for model in models:
#     if 'gpt-4' in model.id:
#         print(model)


MODEL = "gpt-4o"

with open(base_prompt_file, "r") as f:
    base_prompt = f.read()



def encode_image():
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def ask_gpt(base64_image):
    completion = client.chat.completions.create(
        model=MODEL,
        messages= [
            {"role": "system", "content": f"{base_prompt}"},
            {"role": "user", "content": [{"type" : "text", "text": f"{image_question}"},
                                        {"type" : "image_url", "image_url" : {"url" : f'data:image/png;base64,{base64_image}'}}]}
        ]
    )

    answer = completion.choices[0].message.content

    with open("/home/frijol/Desktop/no_recollection/archive-reponses.txt", "a+") as f:
        f.write(f"{answer}\n")
        f.write(f"-----------------\n")

    return(answer)

