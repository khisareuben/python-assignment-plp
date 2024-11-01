# File Creation
f = open("my_file.txt", "w")
text = ["Jonathan", "24", "male", "Sparkle", "25", "female"]

# File Reading and Display
for item in text:
  f.write(item + "\n")
  
f = open("my_file.txt", "r")
print(f.read())

# File Appending:
f = open("my_file.txt", "a")
text1 = ["Power", "Learn", "Project"]
for item in text1:
  f.write(item + "\n")

# Error Handling:
try:
  f = open("my_files.txt", "r")
  print(f.read())
  
except (FileNotFoundError, PermissionError) as e: 
  if isinstance(e, FileNotFoundError): 
    print("File doesn't exist")
  elif isinstance(e, PermissionError): 
    print("You don't have enough permissions")
    
finally:
  print("file closing")
  f.close()
  