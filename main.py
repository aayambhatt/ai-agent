import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY environment variable not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "What is Swiss Re",
        }
    ],
)

if not response.usage:
    raise RuntimeError("API response appears to be malformed")

print("Prompt tokens: ", response.usage.prompt_tokens)
print("Response tokens: ", response.usage.completion_tokens)

print(response.choices[0].message.content)