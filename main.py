import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


def generate_content(client, messages):
    """Generate content using the OpenRouter API and return the response.
    
    Args:
        client: OpenAI client configured for OpenRouter
        messages: List of message dictionaries for the conversation
        
    Returns:
        OpenAI response object containing the generated content
        
    Raises:
        RuntimeError: If the API response is malformed
    """
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )
    
    if not response.usage:
        raise RuntimeError("API response appears to be malformed")
    
    return response


# Input: parse command line arguements
parser = argparse.ArgumentParser(description="AI bot")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
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

# create the messages list variable
messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]

# Process: pass the captured variable into api call using the helper function
response = generate_content(client, messages)

# output: Validate and print results
if args.verbose:
    print(f"User prompt: {args.user_prompt}" )
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

print(response.choices[0].message.content)