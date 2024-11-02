import os
import shutil

path=input("Enter your path :")
files=os.listdir(path)

for i in files:
  filename,extension=os.path.splitext(i)
  extension_1= extension[1:]

  folder=path+"//"+extension_1
  if os.path.exists(folder):
    shutil.move(path+"//"+i , path+"//"+extension_1+"//"+i)
  else:
    os.makedirs(folder)
    shutil.move(path+"//"+i , path+"//"+extension_1+"//"+i)



