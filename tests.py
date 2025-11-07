import unittest
from functions.get_files_info import get_files_info

class GetFileInfo(unittest.TestCase):
  def setUp(self):
    self.get_files_info = get_files_info

  def test_calculator(self):
    result = self.get_files_info("calculator", ".")
    self.assertEqual(result, 
    "Result for current directory:"
    "\n - main.py: file_size=729 bytes, is_dir=False"
    "\n - pkg: file_size=160 bytes, is_dir=True"
    "\n - tests.py: file_size=1342 bytes, is_dir=False"
    )

  def test_slash_bin(self):
    result = self.get_files_info("calculator", "..")
    self.assertEqual(result, 
    """
    Result for '/bin' directory:
    Error: Cannot list "/bin" as it is outside the permitted working directory
    """)

if __name__ == "__main__":
    unittest.main()