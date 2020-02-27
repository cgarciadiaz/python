#file dialog
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
#copy files
import shutil
#system
import os
#explorer
import subprocess
subprocess.Popen(r'explorer "C:\Users\itach\Documents\TORRENTS\DESCARGAS COMPLETAS"')
#control time
import time

#source folder
source = filedialog.askdirectory(parent=root,initialdir="C:\\Users\itach\Documents\TORRENTS\DESCARGAS COMPLETAS",title='Please select source directory')
print(source)

#calculation of folder size
folder_size = 0
for (path, dirs, files) in os.walk(source):
  for file in files:
    filename = os.path.join(path, file)
    folder_size += os.path.getsize(filename)
print ("Folder = %0.1f MB" % (folder_size/(1024*1024.0)) )
print ("Folder = %0.1f GB" % (folder_size/(1024*1024*1024.0)) )

#destination folder
destination = filedialog.askdirectory(parent=root,initialdir="D:\\MULTIMEDIA",title='Please select destination directory')
print(destination)

#move files
start_time = time.time()
move_files = shutil.move(source, destination)
print("finish")

end_time = time.time()

final_time =  end_time-start_time
print ("Folder = %0.1f MB" % (folder_size/(1024*1024.0)) )
print ("Folder = %0.1f GB" % (folder_size/(1024*1024*1024.0)) )
print("Finish move files in ",final_time/60, "minutes or ",final_time," seconds")