import openai
import requests
import uuid
import sys

openai.api_key = open("API_KEY" , "r").read()

text = ""

if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
else:
    print("No prompt provided.")

response = openai.Image.create(
  prompt=text,
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']

image_data = requests.get(image_url).content

with open(str(uuid.uuid4().hex) + '.jpg', 'wb') as handler:
    handler.write(image_data)