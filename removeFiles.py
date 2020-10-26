import os, time, sys
import shutil


path = r"C:/Users/Aswin  A Arun/Downloads"


now = time.time()
ctime = os.stat(path).st_ctime

for f in os.listdir(path):

 if os.stat(f).st_ctime


  if os.path.isfile(f):

   os.remove(os.path.join(path, f))

