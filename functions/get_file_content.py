import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
  relative_path = os.path.join(working_directory, file_path)
  absolute_path = os.path.abspath(relative_path)
  file_name = absolute_path.split(os.sep)[-1]
  error = ''

  if working_directory not in absolute_path:
    error = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  
  if not os.path.isfile(absolute_path):
    error = f'Error: File not found or is not a regular file: "{file_path}"'

  if error:
    return error  
  
  def read_files_content():
    try:
      with open(absolute_path, "r") as f:
          full_file = f.read()

      with open(absolute_path, "r") as f:
          truncated_file = f.read(MAX_CHARS)

      if len(full_file) > MAX_CHARS:
          return truncated_file + f'[...File "{file_path}" truncated at 10000 characters]'

      return full_file
    
    except (OSError, TypeError, ValueError) as err:
      return f'Error: An error occurred:\n {err}'

  return f"Content of {file_name}:\n{read_files_content()}"

# Function schema: Tells the LLM how to use the function.
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a given file. Does only work for filepaths relativ inside the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file from wich to get the content from. When not given or pointing to a directory is returns an error. Only files inside the working directory or files in subdirectories of the working directory are allowed.",
            ),
        },
    ),
)