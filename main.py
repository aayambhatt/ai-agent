import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


# Input: parse command line arguements
parser = argparse.ArgumentParser(description="AI bot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

# Load env variables and initialise client
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY environment variable not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Process: pass the captured variable into api call
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ],
)

# output: Validate and print results
if not response.usage:
    raise RuntimeError("API response appears to be malformed")

print("Prompt tokens: ", response.usage.prompt_tokens)
print("Response tokens: ", response.usage.completion_tokens)

print(response.choices[0].message.content)