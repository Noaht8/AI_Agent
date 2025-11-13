import os

def get_file_content(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_directory_abs = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target is inside working_directory
        if not target_directory_abs.startswith(working_directory_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_directory_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10000

        with open(target_directory_abs, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                return file_content_string[:10001] + f'[...File "{file_path}" truncated at 10000 characters]'
            else:
                return file_content_string

    except Exception as e:
        return f"Error: {e}"


            


