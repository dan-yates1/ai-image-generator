import openai
import requests
import uuid

openai.api_key = open("API_KEY" , "r").read()

response = openai.Image.create(
  prompt="spaceship flying through space 4k ultra hd",
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']

image_data = requests.get(image_url).content

with open(str(uuid.uuid4().hex) + '.jpg', 'wb') as handler:
    handler.write(image_data)