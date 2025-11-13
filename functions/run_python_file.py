import os

def run_python_file(working_directory, file_path, args=[]):
    try:
        # Absolute paths
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure the file is inside the working directory
        if not target_file_abs.startswith(working_dir_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Ensure file exists
        if not os.path.isfile(target_file_abs):
            return f'Error: File "{file_path}" not found.'

        # Ensure it is a Python file
        if not target_file_abs.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'


    except Exception as e:
        return f"Error: {e}"

