#File Removal code
#What we want to do is create a program to delete files

  #Import Shutil
import os
import shutil

  #Give the path
path = "C:/Users/vaibh/Desktop/WhiteHat VS Code/AVSC Projects/Project 99- File Removal"
path1 = "C:/Users/vaibh/Desktop/WhiteHat VS Code/AVSC Projects/Project 99- File Removal/a.txt"
path2 = "C:/Users/vaibh/Desktop/WhiteHat VS Code/AVSC Projects/Project 99- File Removal/e.txt"
path3 = "C:/Users/vaibh/Desktop/WhiteHat VS Code/AVSC Projects/Project 99- File Removal/hi.jpg"

  #Does path exist?
a = os.path.exists(path)
b = os.path.exists(path1)
c = os.path.exists(path2)
d = os.path.exists(path3)

print(a) #True
print(b) #True
print(c) #True
print(d) #True

print("The files before removal: " + str(os.listdir(path)))

os.remove(path1)
os.remove(path2)
os.remove(path3)

print("The files left after removal: "+ str(os.listdir(path)))