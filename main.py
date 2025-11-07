import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import schema_get_files_info

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
    user_prompt = " ".join(args)
    
    # The system prompt is passed to the LLM, so that the user can't do "anything"
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # All the functions we wanna allow the LLM to use.
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )

    # Send content to LLM and get response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt)
        )
    
    # Print function calls
    if response.function_calls is not None:
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:     
        # Print LLM text response
        print(response.text)

    
    # Output verbose response and token usage
    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    return 0

if __name__ == "__main__":
    main()
