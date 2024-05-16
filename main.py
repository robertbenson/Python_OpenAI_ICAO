from openai import OpenAI
from dotenv import load_dotenv
import os
client = OpenAI()

load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")

completion = client.chat.completions.create(
  # model="gpt-3.5-turbo",
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "What ICAO airfields are within 200 km of Dublin airport, return the longitude and latitude of each ?"},
  ]
)

print(completion.choices[0].message.content)