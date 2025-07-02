import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    [app_name, *args] = sys.argv
    verbose = "--verbose" in args
    if verbose:
        args.remove("--verbose")

    if len(args) < 1:
        print(f"Usage: {app_name} <PROMPT>")
        sys.exit(1)

    user_prompt = args[0]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages
    )

    print(response.text)

    if verbose:
        print(f"""User prompt: {user_prompt}
Prompt tokens: {response.usage_metadata.prompt_token_count}
Response tokens: {response.usage_metadata.candidates_token_count}
""")


if __name__ == "__main__":
    main()
