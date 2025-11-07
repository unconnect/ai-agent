import os
import subprocess
from config import ALLOWED_FILE_EXTENSIONS, TIMEOUT

def run_python_file(working_directory, file_path, args=[]):
  relative_path = os.path.join(working_directory, file_path)
  absolute_path = os.path.abspath(relative_path)
  (head, tail) = os.path.split(absolute_path)
  (root, extension) = os.path.splitext(tail)

  error = ''

  if working_directory not in absolute_path:
    error = f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

  if not os.path.exists(absolute_path):
    error = f'Error: File "{file_path}" not found.'

  if extension not in ALLOWED_FILE_EXTENSIONS:
    error = f'Error: "{file_path}" is not a Python file.'

  if error:
    return error  
  
  try:
    cp = subprocess.run(["python3", absolute_path, *args], timeout=TIMEOUT, capture_output=True)

    formatted_result = f'STDOUT: {cp.stdout}, STDERR: {cp.stderr}' 
    exit_code = f'Process exited with code {cp.returncode}'
    no_output = 'No output produced'

    if not cp.stdout:
      return no_output
    
    if cp.returncode != 0:
      return exit_code
    
    return formatted_result
  
  except BaseException as err:
    return f"Error: executing Python file: {err}"

