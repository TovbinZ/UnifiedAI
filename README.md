Simple_AI
=========

Simple_AI is a Python package that simplifies interaction with multiple AI APIs by providing a single, unified API. Currently, it supports OpenAI, Anthropic, and Google AI APIs.


## Features

- Single API for multiple AI providers
- Easy switching between different AI models
- Simplified authentication and API key management
- Built-in error handling and rate limiting


Installation
============


    pip install simple_ai


Usage
========


usage and methods of using one AI instance

```

    from Simple_AI.simple import *


    API = AI("Instance Name","OPENAI_API_KEY"),"gpt-4o")
    
    #default is "You are a helpful assistant"
    API.set_instructions("You are a sarcastically helpful assistant.")


    #defualt is 512
    API.set_max_tokens(100)


    # add context without an api call
    API.add_context("My Name is John.")


    print(API.get_response("what is my name?"))

    
    #history is a list object of all the user 
    print(AI.history())
    
```

Use multiple AI instances at once using a Batch Instance


```
from Simple_AI.simple import *
import pprint

gpt = AI("OPENAI_API_KEY","gpt-4o")
claude = AI("ANTHROPIC_API_KEY","claude-3-5-sonnet-latest")
gemeni = AI("GEMINI_API_KEY","gemini-1.5-pro")


models  = Batch([gpt, claude, gemeni])

models.set_instructions("You are a sarcastically helpful assistant.")

models.set_max_tokens(100)

models.add_context("My name is John.")



# get_response returns a dictionary object with
# the model names and their responses
pprint.pp(models.get_response("What is my name?"))




```








