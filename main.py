import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info


def main():
    messages = [types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),]

    system_prompt = """
        You are a helpful AI coding agent.
        
        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
        
        - List files and directories
        
        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is auto        matically injected for security reasons.
        """

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    available_functions = types.Tool(function_declarations=[schema_get_files_info,])

    response = client.models.generate_content(model="gemini-2.0-flash-001",contents=messages,config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt),)
    

    # print(response.text)
    if response.function_calls:
        for funct in response.function_calls:
            print(f"Calling function: {funct.name}({funct.args})")
    else:
        print(response.text)
    
    if "--verbose" in sys.argv:
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")




if __name__ == "__main__":
    main()
