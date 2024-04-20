import json
from datetime import datetime, date

class OPENAI_CHAT_COMPLETION_RESPONSE:
    def __init__(self, response_filename="DB/openai_data/openai_api_responses.json", summary_filename="DB/openai_data/summary.json"):
        self.response_filename = response_filename
        self.summary_filename = summary_filename
    
    def save_response(self, data):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with open(self.response_filename, "r+") as json_file:
                saved_data = json.load(json_file) 
        except FileNotFoundError:
            saved_data = {}
        
        saved_data.setdefault("openai_api_chatCompletion_response", []).append({current_datetime: data})
        
        with open(self.response_filename, "w+") as json_file:
            json.dump(saved_data, json_file, indent=4)
            
    def extract_and_summarize_usage(self, response):
        current_date = date.today().strftime("%Y-%m-%d")  # Poprawiono na bieżącą datę
        token_usage = response["usage"]["total_tokens"]
        
        # Load or create the summary data
        try:
            with open(self.summary_filename, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}
        
        # Update token usage
        token_usage_data = data.setdefault("token_usage", {})
        token_usage_data[current_date] = token_usage_data.get(current_date, 0) + token_usage
        
        # Update responses count
        responses_count = data.get("responses_count", 0) + 1
        data["responses_count"] = responses_count
        
        # Save the summary data to the JSON file
        with open(self.summary_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
    def init(self, response):
        self.save_response(response)
        self.extract_and_summarize_usage(response)


"""
# Sample response
response = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
                "role": "assistant"
            },
            "logprobs": None
        }
    ],
    "created": 1677664795,
    "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
    "model": "gpt-3.5-turbo-0613",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 17,
        "prompt_tokens": 57,
        "total_tokens": 74
    }
}

x = OPENAI_CHAT_COMPLETION_RESPONSE()

x.save_response(response)
token_usage, responses_count = x.extract_and_summarize_usage(response)
print("Token Usage:", token_usage)
print("Responses Count:", responses_count)
"""
