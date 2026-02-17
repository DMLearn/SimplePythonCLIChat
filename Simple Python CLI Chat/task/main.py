"""
Simple Python CLI Chat Application

A command-line chatbot powered by OpenAI's GPT-4o-mini that demonstrates:
- Interactive chat loop with conversation history
- Function calling (tool use) for chat termination
- Token usage tracking and cost calculation
- Environment-based configuration
"""

import os
from openai import OpenAI
from dotenv import load_dotenv


# ============================================================================
# Configuration
# ============================================================================

# Load environment variables from .env file
load_dotenv()

# System prompt that defines the assistant's behavior
SYSTEM_PROMPT = (
    "You are an helpful assistant for a simple CLI chat. "
    "Only respond with text messages. Get creative with the answers!"
)

# Pricing for GPT-4o-mini (as of February 2026)
# https://openai.com/api/pricing/
INPUT_COST_PER_MILLION = 0.150  # $0.150 per 1M input tokens
OUTPUT_COST_PER_MILLION = 0.600  # $0.600 per 1M output tokens

# Model to use for chat completions
MODEL = "gpt-4o-mini"


# ============================================================================
# OpenAI Client Initialization
# ============================================================================

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)


# ============================================================================
# Function Definitions (Tools)
# ============================================================================

# Define tools that the assistant can call
# The end_chat function allows the assistant to terminate the conversation
# when the user requests to exit
tools = [
    {
        "type": "function",
        "function": {
            "name": "end_chat",
            "description": "Ends the chat session when the user wants to exit or terminate the conversation",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


# ============================================================================
# Helper Functions
# ============================================================================

def calculate_cost(input_tokens: int, output_tokens: int) -> float:
    """
    Calculate the total cost of an API call based on token usage.

    Args:
        input_tokens: Number of tokens in the prompt
        output_tokens: Number of tokens in the completion

    Returns:
        Total cost in USD
    """
    input_cost = (input_tokens / 1_000_000) * INPUT_COST_PER_MILLION
    output_cost = (output_tokens / 1_000_000) * OUTPUT_COST_PER_MILLION
    return input_cost + output_cost


def display_interaction(user_message: str, assistant_message: str, cost: float):
    """
    Display a single interaction with formatted output.

    Args:
        user_message: The user's input message
        assistant_message: The assistant's response
        cost: The cost of the API call
    """
    print(f"You: {user_message}")
    print(f"Assistant: {assistant_message}")
    print(f"Cost: ${cost:.6f}")
    print()


# ============================================================================
# Main Chat Loop
# ============================================================================

def main():
    """
    Main function that runs the interactive chat loop.
    Maintains conversation history and handles function calls.
    """
    # Initialize conversation history with system prompt
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("Chat started! Ask the assistant to 'end chat' or 'exit' when you're done.\n")

    # Continuous interaction loop
    while True:
        # Get user input
        user_prompt = input("Enter a message: ")

        # Add user message to conversation history
        messages.append({
            "role": "user",
            "content": user_prompt
        })

        # Send request to OpenAI API
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools
        )

        # Extract assistant's message from response
        assistant_message = response.choices[0].message

        # Check if assistant called the end_chat function
        if assistant_message.tool_calls:
            tool_call = assistant_message.tool_calls[0]

            if tool_call.function.name == "end_chat":
                # Display final interaction
                assistant_text = assistant_message.content if assistant_message.content else "Goodbye!"
                print(f"You: {user_prompt}")
                print(f"Assistant: {assistant_text}")
                print(f"Function call ID: {tool_call.id}")

                # Calculate and display cost
                cost = calculate_cost(
                    response.usage.prompt_tokens,
                    response.usage.completion_tokens
                )
                print(f"Cost: ${cost:.6f}")

                # Exit the loop
                break

        # Display the interaction
        display_interaction(
            user_prompt,
            assistant_message.content,
            calculate_cost(
                response.usage.prompt_tokens,
                response.usage.completion_tokens
            )
        )

        # Add assistant's response to conversation history
        messages.append({
            "role": "assistant",
            "content": assistant_message.content
        })


# ============================================================================
# Entry Point
# ============================================================================

if __name__ == "__main__":
    main()
