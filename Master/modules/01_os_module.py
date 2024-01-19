import os

# current working directory
print(os.getcwd())

# change current working directory
os.chdir("D:\My coding files\python journey\Begineer")

print(os.getcwd())

with open("highscore.txt") as f:
    pass

# list the files of current directory
print(os.listdir())
print(os.listdir("D:\My coding files\python journey\Begineer"))

# make directory in the current directory folder
os.mkdir("newfile.py")

# make directories i.e. directory inside of directory
os.makedirs("this/that")

# remove directory
os.rmdir("newfile.py")

# remove directories
os.removedirs("this/that")

# rename the file
os.rename("abcde.py", "niroj.txt")

# get the environment variables
print(os.environ.get("path"))

# join the path
print(os.path.join("D:/My coding files/", "/python journey/Begineer"))

# checks whether the path exists or not
print(os.path.exists("C:/Program Files"))

# is file or isdir
print(os.path.isdir("C:/ProgramData"))
print(os.path.isfile("C://ProgramData"))

