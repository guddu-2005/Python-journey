# Label the program written in problem 4 with comments.

# immport os module
import os

# use os to find all the directory content
directory_path = '/'

# use os.listdir to list all the content from directory
contents = os.listdir(directory_path)

# use to print the content
for items in contents :
    print(items)