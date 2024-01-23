"""
This module contains an example for how to send a API call to an LLM, as well
as a function at the bottom of the file marked TODO, where you will send a request to the
API yourself. It should be very similar to the provided example.
"""
import os
import requests

"""
All requests to the LLM require some form of a key.
Other sensitive data has also been hidden through environment variables.
"""
base_url = os.environ['LLM_ENDPOINT']
api_key = os.environ['HF_TOKEN']
"""
This function sends an HTTP request to an LLM which will prompt it for some
generic response. The function will return the response JSON. The URL used here has
been hidden via environment variables, but the general pattern is constructed as a POST to a URL
on which the LLM is being hosted.

Let's also take a look at what else is provided here.
    - standard HTTP POST request, which sends a JSON body. We should receive a JSON body in the response.
    - an api key for accessing the provided URL is set in the header
    - the request body will contain some input text, as well as any LLM parameters
    (eg number of tokens, temperature, etc)
    - the response body, apart from metadata for the chat message, contains the
        LLM's response under a 'content' field, which you can see by running the full script from
        app.py.
        
An API call to different LLM APIs, such as to OpenAI, HuggingFace, LLaMa, etc may be formatted slightly
differently.
"""


def sample():
    res = requests.post(f"{base_url}",
                        headers={
                            "Content-Type": "application/json",
                            "Authorization": f"Bearer {api_key}"
                        },
                        json={
                            "inputs": "Sample of a text input sent to the LLM. Parameters are set below.",
                            "parameters": {
                                "max_new_tokens": 400,
                                "temperature": 1
                            }
                        })
    print(res)
    return res


"""
TODO: Within this function, send a request using the same URL & API key as above
where the user prompts the LLM to produce a hello world response, and return the resulting response. 
Test cases will verify that the LLM has actually produced some text containing "hello world".
"""


def lab():
    return "todo"
