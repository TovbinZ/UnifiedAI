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


Creating an AI instance
```python

    API = AI(instance_name,api_key,model_name)

```

usage and methods of using one AI instance

```python  
    from Simple_AI.simple import *

    API = AI("gpt4","OPENAI_API_KEY","gpt-4o")


    #default is "You are a helpful assistant"
    API.set_instructions("You are a sarcastically helpful assistant.")


    #defualt is 512
    API.set_max_tokens(100)


    # add context without an api call
    API.add_context("My Name is John.")


    print(API.get_response("what is my name?"))

    
    #history is a list object of all the user messages and assistant responses. 
    print(AI.history())
    
```

Use multiple AI instances at once using a Batch Instance.


```python
    
    from Simple_AI.simple import *
    import pprint

    gpt = AI("gpt","OPENAI_API_KEY","gpt-4o")
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

Use multiple of the same AI instances at once.


```python

    from Simple_AI.simple import *
    import pprint

    angry = AI("angry","OPENAI_API_KEY","gpt-4o")
    sarcastic = AI("sarcastic","OPENAI_API_KEY","gpt-4o")
    sad = AI("sad","OPENAI_API_KEY","gpt-4o")

    angry.set_instructions("Answer in a angry way.")

    sarcastic.set_instructions("Answer in a sarcastic way.")

    sad.set_instructions("Answer in a sad way")


    emotions = Batch([angry,sarcastic,sad])


    emotions.set_max_tokens(100)

    pprint.pp(emotions.get_response("What is 1 + 1?"))


```
