import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open("newfile.txt", "w") as f:
    pass
  timestamp = os.path.getmtime("newfile.txt")
  # Convert the timestamp into a readable format, then into a string
  timestamp = datetime.datetime.fromtimestamp(timestamp).isoformat()
  # Return just the date portion 
  date = timestamp[:10]
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(date))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
