import os
def get_files_info(working_directory, directory="."):
  relative_path = os.path.join(working_directory, directory)
  absolute_path = os.path.abspath(relative_path)
  work_dir_content = os.listdir(absolute_path)

  if directory not in absolute_path:
    error = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    # print(error)
    return error

  # print("_______DEBUG_______")
  # print(f"working_directory, directory: {working_directory}, {directory}")
  # print(f"relative_path: {relative_path}")
  # print(f"absolute_path: {absolute_path}")
  # print(f"work_dir_content: {work_dir_content}")
  # print("_______DEBUG_______")

  def compute_entry_infos():
      entries_infos = []
      for entry in work_dir_content:
        entry_path = os.path.join(absolute_path, entry)
      
        entries_infos.append(f" - {entry}: file_size={os.path.getsize(entry_path)} bytes, is_dir={os.path.isdir(entry_path)}")
      
      entries_infos.sort()

      return "\n".join(entries_infos)
      

  return f"Result for current directory:\n{compute_entry_infos()}"