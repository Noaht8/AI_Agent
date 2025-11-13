import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file



def main():
    messages = [types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),]

    system_prompt = """
        You are a helpful AI coding agent.
        
        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
        
        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files
        
        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is auto        matically injected for security reasons.
        """

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    available_functions = types.Tool(function_declarations=[schema_get_files_info,schema_get_file_content,schema_run_python_file,schema_write_file, ])

    response = client.models.generate_content(model="gemini-2.0-flash-001",contents=messages,config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt),)
    
    verbose = "--verbose" in sys.argv 

    # print(response.text)
    if response.function_calls:
        for funct in response.function_calls:
            print(f"Calling function: {funct.name}({funct.args})")
    else:
        print(response.text)


    if response.function_calls:
        for func_call in response.function_calls:
            function_call_result = call_function(func_call, verbose=verbose)

        # Check if result has a function response
            if not hasattr(function_call_result.parts[0], "function_response"):
                raise RuntimeError("Fatal: Missing function response")

            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    
    if "--verbose" in sys.argv:
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



def call_function(function_call_part, verbose=False):
    """
    Dispatch function to call one of our registered tool functions dynamically.
    """

    function_name = function_call_part.name
    function_args = dict(function_call_part.args or {})

    # Always add the working directory manually
    function_args["working_directory"] = "./calculator"

    # If verbose, print details
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    # Map function names to actual function objects
    available_functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    # Check if function exists
    if function_name not in available_functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    try:
        # Call the function dynamically
        func_to_call = available_functions[function_name]
        function_result = func_to_call(**function_args)
    except Exception as e:
        function_result = f"Error: executing function {function_name}: {e}"

    # Build the tool response
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )




if __name__ == "__main__":
    main()
