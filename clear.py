import os
import shutil

output_dir = "D:/AppRelease/OspreyInspectFolder"

for i in range(10):
    if i > 0:
        dir = output_dir + str(i)
    else:
         dir = output_dir
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        os.remove(file_path)
