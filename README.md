# Simple Python CLI Chat

A command-line chatbot application powered by OpenAI's GPT-4o-mini API. This project demonstrates how to build an interactive chat interface with conversation history, function calling (tool use), and token cost tracking.

## Features

- **Interactive Chat Loop**: Continuous conversation with the AI assistant
- **Conversation History**: Maintains context across multiple interactions
- **Function Calling**: Demonstrates OpenAI's function calling feature with a custom `end_chat` tool
- **Token Cost Tracking**: Calculates and displays the cost of each API interaction
- **Environment Configuration**: Secure API key management using environment variables

## What I Learned

This project helped me understand:

1. **OpenAI API Integration**
   - Setting up the OpenAI Python client
   - Using the Chat Completions API
   - Managing conversation history with message roles (system, user, assistant)

2. **Function Calling (Tool Use)**
   - Defining custom functions/tools for the AI to use
   - Implementing function call detection and handling
   - Understanding when and how the model decides to call functions

3. **Token Management**
   - Tracking token usage for cost optimization
   - Calculating API costs based on input/output tokens
   - Understanding the pricing model for GPT-4o-mini

4. **Best Practices**
   - Environment variable management with `python-dotenv`
   - Clean code organization with functions and constants
   - Proper documentation and code comments
   - Type hints for better code clarity

## Prerequisites

- Python 3.7+
- OpenAI API key
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Simple-Python-CLI-Chat
```

2. Install required dependencies:
```bash
pip install openai python-dotenv
```

3. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_api_key_here
BASE_URL=https://api.openai.com/v1  # Optional: custom base URL
```

## Usage

Run the chat application:
```bash
python main.py
```

### Example Interaction

```
Chat started! Ask the assistant to 'end chat' or 'exit' when you're done.

Enter a message: Hello! What can you help me with?
You: Hello! What can you help me with?
Assistant: Hello! I'm your friendly CLI chat assistant. I can help you with various tasks, answer questions, have conversations, or just chat about anything you'd like. What's on your mind today?
Cost: $0.000123

Enter a message: Tell me a fun fact about Python
You: Tell me a fun fact about Python
Assistant: Here's a fun fact: Python was named after the British comedy series "Monty Python's Flying Circus," not the snake! Guido van Rossum, Python's creator, was a fan of the show and wanted a short, unique name that was slightly mysterious.
Cost: $0.000156

Enter a message: Please end the chat
You: Please end the chat
Assistant: Goodbye! It was great chatting with you!
Function call ID: call_abc123xyz
Cost: $0.000098
```

## Project Structure

```
Simple-Python-CLI-Chat/
├── main.py           # Main application file
├── .env              # Environment variables (not in repo)
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## Key Concepts

### 1. Chat Completions API
The application uses OpenAI's Chat Completions API to generate responses. Each request includes:
- System prompt: Defines the assistant's behavior
- Conversation history: Previous messages for context
- Tools: Functions the assistant can call

### 2. Function Calling
The `end_chat` function demonstrates OpenAI's function calling feature:
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "end_chat",
            "description": "Ends the chat session when the user wants to exit",
            "parameters": {...}
        }
    }
]
```

When the user asks to exit, the model recognizes this intent and calls the function.

### 3. Token Cost Calculation
Cost is calculated based on GPT-4o-mini pricing:
- Input tokens: $0.150 per 1M tokens
- Output tokens: $0.600 per 1M tokens

```python
cost = (input_tokens / 1_000_000) * 0.150 + (output_tokens / 1_000_000) * 0.600
```

## Configuration

You can customize the following parameters in `main.py`:

- `SYSTEM_PROMPT`: Change the assistant's personality and behavior
- `MODEL`: Switch to a different OpenAI model (e.g., "gpt-4")
- `INPUT_COST_PER_MILLION` / `OUTPUT_COST_PER_MILLION`: Update pricing if changed

## Error Handling

The application requires:
- Valid `OPENAI_API_KEY` in the `.env` file
- Active internet connection
- Sufficient OpenAI API credits

## Future Enhancements

Possible improvements:
- Add conversation export (save chat history to file)
- Implement streaming responses for real-time output
- Add support for multiple tools/functions
- Include error handling and retry logic
- Add conversation statistics (total tokens, total cost)
- Support for different OpenAI models selection at runtime

## Dependencies

- `openai`: Official OpenAI Python library
- `python-dotenv`: Load environment variables from `.env` file

## License

This project is open source and available for educational purposes.

## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI Pricing](https://openai.com/api/pricing/)

## Contact

Feel free to reach out if you have questions or suggestions!

---

*Built as a learning project to understand OpenAI API integration and function calling.*
