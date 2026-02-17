import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

system_prompt = "You are an helpful assistant for a simple CLI chat. Only respond with text messages. Get creative with the answers!"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

# Prompt user for input
user_prompt = input("Enter a message: ")

# Send request to GPT API
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)

# Display user's message
print(f"You: {user_prompt}")

# Display assistant's response
print(f"Assistant: {response.choices[0].message.content}")

# Calculate and display token cost
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens

# GPT-4o-mini pricing: $0.150 per 1M input tokens, $0.600 per 1M output tokens
input_cost = (input_tokens / 1_000_000) * 0.150
output_cost = (output_tokens / 1_000_000) * 0.600
total_cost = input_cost + output_cost

print(f"Cost: ${total_cost:.6f}")
