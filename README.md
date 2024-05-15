# OpenAI demo 
## Create an OpenAI account

[OpenAI Quickstart](https://platform.openai.com/docs/quickstart)


set up an OPENAI API KEY
### Model


OpenAI has different model offerings and price points. [models and price points](https://platform.openai.com/docs/models)
### Pip 


```python
pip install python_dotenv`
```

```python
pip install --upgrade openai
```

### Python Code

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
## Find airport ICAO codes within 200km of Dublin.

### OpenAI Generated Output 


Dublin Airport (IATA: DUB, ICAO: EIDW) is located in Ireland, near the city of Dublin. Within a radius of 200 kilometers, there are several other airfields with ICAO codes. Here are some notable ones:

1. **Shannon Airport (ICAO: EINN)** - Approximately 190 km southwest of Dublin.
2. **Cork Airport (ICAO: EICK)** - Approximately 220 km south-southwest of Dublin, slightly outside the 200 km range but often included due to its proximity.
3. **Knock Ireland West Airport (ICAO: EIKN)** - Approximately 180 km northwest of Dublin.
4. **Waterford Airport (ICAO: EIWF)** - Approximately 130 km south of Dublin.
5. **Belfast International Airport (ICAO: EGAA)** - Approximately 140 km north of Dublin, in Northern Ireland.
6. **Belfast City Airport (George Best Belfast City Airport, ICAO: EGAC)** - Approximately 145 km north of Dublin, also in Northern Ireland.
7. **Donegal Airport (ICAO: EIDL)** - Approximately 180 km northwest of Dublin.

These are some of the primary airports with ICAO codes within the specified range of Dublin Airport. There are also several smaller airfields and airstrips, which may not have regular commercial services but serve as important points for general aviation, flight training, and private flights.
`