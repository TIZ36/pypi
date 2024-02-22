import ollama

stream = ollama.chat(model='llama2', messages=[
    {
        "role": "user",
        "content": "Hello, how are you?"
    }
],
stream=True)

for chunk in stream:
    print(chunk['message']['content'], end=' | ', flush=True)