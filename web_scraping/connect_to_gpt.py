import openai
from openai.types.chat.completion_create_params import ResponseFormat
import json
from api import API
from openai_api_usage import OPENAI_CHAT_COMPLETION_RESPONSE

save_openai_uage = OPENAI_CHAT_COMPLETION_RESPONSE()
openai.api_key = API().get_api("apis.json")[0]["OPENAI_API_KEY"]

completion1 = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k-0613",
  messages=[
    {"role": "system", "content": "Jesteś systemem wymyslajacym jednozdaniowe zagadki"},
  ]
)
completion = openai.chat.completions.create(
  model="gpt-3.5-turbo-16k-0613",
  messages=[
    {"role": "system", "content": "Odpowiadasz na pytania albo zagadki"},
    {"role": "user", "content": completion1.choices[0].message.content}
  ]
)

def save_helper(data):
    return json.loads(data.to_json())

save_openai_uage.init(save_helper(completion))

#print(completion1.choices[0].message.content)
#print(completion.choices[0].message.content)