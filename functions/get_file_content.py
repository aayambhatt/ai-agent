import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        # Get absolute path of working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct and normalize the full path to target file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Validate target file is within working directory
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if it's actually a file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the file content
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)

            # Check if file was truncated
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {str(e)}"