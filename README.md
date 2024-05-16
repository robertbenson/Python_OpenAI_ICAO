# OpenAI demo using Python
## Task: 
### "What ICAO airfields are within 200 km of Dublin airport, return the longitude and latitude of each ?".

This can be tailored to just about anything.

## Create an OpenAI account

[OpenAI Quickstart](https://platform.openai.com/docs/quickstart)


set up an OPENAI API KEY
### Model


OpenAI has different model offerings and price points. [models and price points](https://platform.openai.com/docs/models)
## Install packages


Manage environment variables, sensitive information. Hide the api key from public view for security
```python
pip install python_dotenv  
```
Install or upgrade the OpenAI Python package
```python
pip install --upgrade openai
```

### Python Code 
[sample openai code example](https://platform.openai.com/docs/quickstart/step-3-sending-your-first-api-request)


The supplied openai code has been modified to:
1. use dotenv to hide the api key
2. modify the content for my use case: `"What ICAO airfields are within 200 km of Dublin airport ?"`



```python
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
    {"role": "system", "content": "What ICAO airfields are within 200 km of Dublin airport ?"},
  ]
)

print(completion.choices[0].message.content)
```


### OpenAI Generated Output 


To provide a list of ICAO airfields within 200 km of Dublin Airport (EIDW), I would need to utilize specific aviation databases, mapping tools, or official ICAO resources. However, I'll list a few notable ICAO airfields and their coordinates that are within or near this range:

1. **EIDW (Dublin Airport)**
   - **Latitude:** 53.4213° N
   - **Longitude:** -6.2701° W

2. **EINN (Shannon Airport)**
   - **Latitude:** 52.7019° N
   - **Longitude:** -8.9248° W
   - Distance to Dublin Airport: approximately 192 km

3. **EICK (Cork Airport)**
   - **Latitude:** 51.8413° N
   - **Longitude:** -8.4911° W
   - Distance to Dublin Airport: approximately 220 km (slightly beyond 200 km but close)

4. **EGAC (George Best Belfast City Airport)**
   - **Latitude:** 54.6181° N
   - **Longitude:** -5.8725° W
   - Distance to Dublin Airport: approximately 140 km

5. **EGAA (Belfast International Airport)**
   - **Latitude:** 54.6575° N
   - **Longitude:** -6.2158° W
   - Distance to Dublin Airport: approximately 160 km

6. **EINN (Shannon Airport)**
   - **Latitude:** 52.7019° N
   - **Longitude:** -8.9248° W
   - Distance to Dublin Airport: approximately 204 km (slightly beyond 200 km but close)

Please note that while Shannon and Cork are slightly beyond the 200 km range, I've included them due to their relative proximity. For a comprehensive and precise list of all ICAO airfields within exactly 200 km, accessing a specialized aviation database or mapping software that can provide specific calculations and additional airfields would be necessary.
