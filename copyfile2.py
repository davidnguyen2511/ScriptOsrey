import os
import shutil
import time
from datetime import datetime

source_image = "E:/Scripts/image1.jpg" 

output_dir = "D:/AppRelease/OspreyInspectFolder2"
# for filename in os.listdir(output_dir):
#     file_path = os.path.join(output_dir, filename)
#     os.remove(file_path)
os.makedirs(output_dir, exist_ok=True)

def copy_images():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    for i in range(5):
        new_filename = f"copy_{timestamp}_{i + 1}.jpg"
        destination = os.path.join(output_dir, new_filename)
        shutil.copy(source_image, destination)
        print(f"Created: {destination}")

try:
    while True:
        copy_images()
        time.sleep(0.5)  # 500ms
except KeyboardInterrupt:
    print("Stopped by user.")
