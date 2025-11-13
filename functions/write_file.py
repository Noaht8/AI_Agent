import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_directory_abs = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target is inside working_directory
        if not target_directory_abs.startswith(working_directory_abs):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Ensure the directory for the file exists
        dir_name = os.path.dirname(file_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            with open(target_directory_abs, "w") as f:
                f.write("")  # create empty file
      
        with open(target_directory_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a file within the working directory. Creates the file if it does not exist, overwriting any existing content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to write, within the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write to the file.",
            ),
        },
    ),
)



