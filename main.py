import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    script_name = sys.argv[0]
    # Args without script name
    args = sys.argv[1:]

    if not args:
        print("AI Code Agent 🤖")
        print("Something went wrong! Please give at least one argument!")
        print("\nUsage: $python main.py \"Your prompt goes here”")
        return sys.exit(1)
    
    # Join arguments in case the user does not enclose prompt in quotes
    user_prompt = args[0]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Send content to LLM and get response
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    # Print LLM response
    print(response.text)
    
    # Output verbose response and token usage
    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    return 0

if __name__ == "__main__":
    main()
