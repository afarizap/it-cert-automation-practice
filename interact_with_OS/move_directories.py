import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  os.chdir('..')

  # Return the absolute path of the parent directory
  return os.getcwd()

print(parent_directory())
