import os
from google.genai import types

def get_files_info(working_directory, directory="."):
  relative_path = os.path.join(working_directory, directory)
  absolute_path = os.path.abspath(relative_path)
  work_dir_content = os.listdir(absolute_path)

  if working_directory not in absolute_path:
    error = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    return error

  def compute_entry_infos():
      entries_infos = []
      for entry in work_dir_content:
        entry_path = os.path.join(absolute_path, entry)
      
        entries_infos.append(f" - {entry}: file_size={os.path.getsize(entry_path)} bytes, is_dir={os.path.isdir(entry_path)}")
      
      entries_infos.sort()

      return "\n".join(entries_infos)
      
  return f"Result for current directory:\n{compute_entry_infos()}"

# Function schema: Tells the LLM how to use the function.
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)