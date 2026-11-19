import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        # 1. Get absolute working directory
        working_directory_abs = os.path.abspath(working_directory)

        # 2. Build and normalize target path
        target_path = os.path.normpath(os.path.join(working_directory_abs, file_path))

        # 3. Validate: target inside working directory?
        if os.path.commonpath([working_directory_abs, target_path]) != working_directory_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # 4. Validate: target is not a directory?
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # 5. Ensure parent directories exist
        parent_dir = os.path.dirname(target_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        # 6. Write the file
        with open(target_path, "w") as f:
            f.write(content)

        # 7. Return success message
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        # 8. Return error message
        return f"Error: {str(e)}"
