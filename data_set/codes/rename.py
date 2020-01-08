# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 

# Function to rename multiple files 
path = '/media/solomon/Apps/AI and ML/Audio_Dataset/right'

files = os.listdir(path)

print(enumerate(files))
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(['right'+str(index+1), '.wav'])))

