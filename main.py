import os
from dotenv import load_dotenv
from google import genai
import sys


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():

    script_name = sys.argv[0]
    args = sys.argv[1:]

    # FIXME: Before commit make this more pythionic with "not" keyword. 
    # FIXME: Give an example how to use the cli-tool
    if(len(args) < 1):
        raise SystemExit("Something went wrong! Please give at least one argument!")
    
    # FIXME: Join possible multiple args when not encased in quotes to one arg.
    prompt = args[0]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    return 0

if __name__ == "__main__":
    main()
