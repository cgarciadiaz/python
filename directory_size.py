import os
import subprocess
#file dialog
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

total_size = 0


folder = filedialog.askdirectory(parent=root,initialdir="C:\\",title='Please select directory')
print(folder)

folder_size = 0
for (path, dirs, files) in os.walk(folder):
  for file in files:
    filename = os.path.join(path, file)
    folder_size += os.path.getsize(filename)
print ("Folder = %0.1f MB" % (folder_size/(1024*1024.0)) )
print ("Folder = %0.1f GB" % (folder_size/(1024*1024*1024.0)) )