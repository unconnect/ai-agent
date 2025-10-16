import os
from dotenv import load_dotenv
from google import genai
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
    prompt = " ".join(args)

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    return 0

if __name__ == "__main__":
    main()
