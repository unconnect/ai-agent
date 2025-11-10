import os
from google.genai import types


def write_file(working_directory, file_path, content):
  relative_path = os.path.join(working_directory, file_path)
  absolute_path = os.path.abspath(relative_path)
  file_name = absolute_path.split(os.sep)[-1]
  error = ''

  if working_directory not in absolute_path:
    error = f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  if error:
    return error  

  try:
    # Split given absolute path in head and tail where head the parent
    # dir-path and tail the last segment is. The tail will be our file to 
    # create or write.
    (head, tail) = os.path.split(absolute_path)

    # In case the file_path does not exist we create the parents
    if not os.path.exists(head):
      os.makedirs(head)
    
    # And create a new file and write/overwrite the content to that
    with open(absolute_path, "w") as f:
      result = f.write(content)

      if result > 0:
        return f'Successfully wrote to "{file_path}" ({result} characters written)'



  except (OSError, TypeError, ValueError) as err:
    return f'Error: An error occurred:\n {err}'
  
# Function schema: Tells the LLM how to use the function.
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a given file path. In case the file does not exists the file is created. In case the files already exists the content will be overwritten.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file that should be written or created. Must be within the path of the working directory. ",
            ),
            "content": types.Schema(
              type=types.Type.STRING,
              description="The content to write to the file."
            )
        },
    ),
)