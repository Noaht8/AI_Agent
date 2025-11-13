import os

def get_files_info(working_directory, directory="."):
    try:
        # Compute absolute paths
        working_directory_abs = os.path.abspath(working_directory)
        target_directory_abs = os.path.abspath(os.path.join(working_directory, directory))

        # Ensure target is inside working_directory
        if not target_directory_abs.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if the target is a directory
        if not os.path.isdir(target_directory_abs):
            return f'Error: "{directory}" is not a directory'

        # List contents
        entries = os.listdir(target_directory_abs)
        results = []
        for entry in entries:
            entry_path = os.path.join(target_directory_abs, entry)
            try:
                size = os.path.getsize(entry_path) if os.path.isfile(entry_path) else os.path.getsize(entry_path)
                is_dir = os.path.isdir(entry_path)
                results.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")
            
            except Exception as e:
                results.append(f"- {entry}: Error: {e}")
        result = "\n".join(results)
        return result

    except Exception as e:
        return f"Error: {e}"
