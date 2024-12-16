UnifiedAI
=========

UnifiedAI is a Python package that simplifies the usage of multiple AI APIs by providing a single, unified API. Currently, it supports OpenAI, Anthropic, and Google AI APIs.


## Features

- Single API for multiple AI providers.
- Easy switching between different AI models.
- Simplified authentication and API key management.


Installation
============


    pip install UnifiedAI


Usage
========


Creating an AI instance
```python

API = AI(instance_name,api_key,model_name)

```

Usage and methods of using one AI instance

```python  
from UnifiedAI import *

API = AI("gpt4","OPENAI_API_KEY","gpt-4o")


#default is "You are a helpful assistant"
API.set_instructions("You are a sarcastically helpful assistant.")


#defualt is 512
API.set_max_tokens(100)


# add context without an api call
API.add_context("My Name is John.")


print(API.get_response("what is my name?"))

    
#history is a list object of all the user messages and assistant responses. 
print(API.history)


#print the input token usage of the model
print(API.usage.input_tokens)

#print the output token usage of the model
print(API.usage.output_tokens)


    
```

Use multiple AI instances at once using a Batch instance.


```python
    
from UnifiedAI import *
import json

gpt = AI("gpt","OPENAI_API_KEY","gpt-4o")
claude = AI("claude","ANTHROPIC_API_KEY","claude-3-5-sonnet-latest")
gemeni = AI("gemini","GEMINI_API_KEY","gemini-1.5-pro")


models  = Batch([gpt, claude, gemeni])

models.set_instructions("You are a sarcastically helpful assistant.")

models.set_max_tokens(100)

models.add_context("My name is John.")

# get_response returns a dictionary object with
# the model names and their responses
print(json.dumps(models.get_response("what is my name?"),indent=4))

# print the ouput token usage of each model
print(models.usage["gpt"].output_tokens)
print(models.usage["claude"].output_tokens)
print(models.usage["gemini"].output_tokens)

```

Compare responses with different system instructions. 

```python
from UnifiedAI import *
import json

angry = AI("angry","OPENAI_API_KEY","gpt-4o")
sarcastic = AI("sarcastic","OPENAI_API_KEY","gpt-4o")
sad = AI("sad","OPENAI_API_KEY","gpt-4o")

angry.set_instructions("Answer in a angry way.")
sarcastic.set_instructions("Answer in a sarcastic way.")
sad.set_instructions("Answer in a sad way.")


emotions = Batch([angry,sarcastic,sad])


emotions.set_max_tokens(100)


print(json.dumps(emotions.get_response("what is 1 + 1?"),indent=4))


print(models.usage["angry"].output_tokens)
print(models.usage["sarcastic"].output_tokens)
print(models.usage["sad"].output_tokens)

```
