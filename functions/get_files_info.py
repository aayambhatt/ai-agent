import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
   try:
      # get absolute path of working directory 
      working_dir_abs = os.path.abspath(working_directory)

      # Construct and normalize the full path to target directory
      target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

      # Validate target directory is within working directory
      if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
      # Check if it's actually a directory
      if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
      # Return success message
      return f'Success: "{directory}" is within the working directory'
   except Exception as e:
        return f'Error: {str(e)}'