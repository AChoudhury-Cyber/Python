# Appending to a file
# 'a' adds new values along with the old values in the file
with open("text.txt", "a") as file:
    file.write("\nline 1")

# Writing to a file
# 'w' replaces all of the data in the file
with open("text.txt", "w") as file:
    file.write("\nline 1") 
    file.writelines() # Writes the data as a list in the file

# Reading fril file
with open("text.txt", "r") as file:
    file.read("\nline 1") # Returns a string of the text in the whole file
    file.readlines() # Returns a