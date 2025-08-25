# Open file for writing

with open("notes.txt", "w") as f:
    f.write("This is a sample note.\n")
    f.write("Remember to review Python basics.\n") 

# Appending to a file

with open("notes.txt", "+a") as f:
    f.write("This is a sample note.\n")
    f.write("Remember to review Python basics.\n") 


# File Reading

with open("notes.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)