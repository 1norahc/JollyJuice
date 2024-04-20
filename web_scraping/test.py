import re

class ChatCompletionMessage:
    def __init__(self, content, role, function_call=None, tool_calls=None):
        self.content = content
        self.role = role
        self.function_call = function_call
        self.tool_calls = tool_calls

class Choice:
    def __init__(self, finish_reason, index, logprobs, message):
        self.finish_reason = finish_reason
        self.index = index
        self.logprobs = logprobs
        self.message = message

class CompletionUsage:
    def __init__(self, completion_tokens, prompt_tokens, total_tokens):
        self.completion_tokens = completion_tokens
        self.prompt_tokens = prompt_tokens
        self.total_tokens = total_tokens

class ChatCompletion:
    def __init__(self, id, choices, created, model, object, system_fingerprint, usage):
        self.id = id
        self.choices = choices
        self.created = created
        self.model = model
        self.object = object
        self.system_fingerprint = system_fingerprint
        self.usage = usage

    def parse_message(self, text):
        match = re.match(r"ChatCompletionMessage\(content='(.*?)', role='(.*?)', function_call=(.*?), tool_calls=(.*?)\)", text)
        if match:
            content, role, function_call, tool_calls = match.groups()
            return ChatCompletionMessage(content, role, eval(function_call) if function_call else None, eval(tool_calls) if tool_calls else None)
        else:
            return None

    def parse_choice(self, text):
        match = re.match(r"Choice\(finish_reason='(.*?)', index=(.*?), logprobs=(.*?), message=(.*?)\)", text)
        if match:
            finish_reason, index, logprobs, message_text = match.groups()
            message = self.parse_message(message_text)
            return Choice(finish_reason, int(index), eval(logprobs), message)
        else:
            return None

    def parse_completion(self, text):
        match = re.match(r"ChatCompletion\(id='(.*?)', choices=\[(.*?)\], created=(.*?), model='(.*?)', object='(.*?)', system_fingerprint='(.*?)', usage=(.*?)\)", text)
        if match:
            id, choices_text, created, model, object, system_fingerprint, usage_text = match.groups()
            choices = [self.parse_choice(choice_text.strip()) for choice_text in choices_text.split(",")]
            usage = eval(usage_text)
            return ChatCompletion(id, choices, int(created), model, object, system_fingerprint, usage)
        else:
            return None

# Przykładowe dane w formacie tekstu
data_text = "ChatCompletion(id='chatcmpl-9G3F1xFXCGAKNrKSwFjlnzwEDKxac', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Chmura może lecieć, ale nie posiada skrzydeł.', role='assistant', function_call=None, tool_calls=None))], created=1713612735, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_c2295e73ad', usage=CompletionUsage(completion_tokens=17, prompt_tokens=40, total_tokens=57))"

# Parsowanie danych
parsed_data = ChatCompletion().parse_completion(data_text)

# Wyświetlenie słownika
print(vars(parsed_data))
