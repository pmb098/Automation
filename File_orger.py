import os
import shutil

source='C:\\Users\\Pavitra'
dest ='C:\\Desktop'

file_types = {
    'image':['jpg,','png', 'gif','jpeg'],
    'doc' : ['pdf','docx', 'txt', 'xlsx'],
    'videos' : ['mp4', 'mkv', 'avi'],
    'audio' : ['mp3','wav','flac']    
    }

for folder in file_types.keys():
    os.makedirs(os.path.join(dest,folder))
    print(folder)
    
def organize_files():
    for filename in os.listdir(source):
        filepath=os.path.join(source, filename)
        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            ext =ext [1:].lower()
            
            folder=None
            for catagary , extensions in file_types.items():      
                if ext in extensions:
                    folder = catagary
                    break
                
            if folder:
                new_path =os.path.join(dest, folder, filename)
                shutil.copy(filepath, new_path)
                print(f'moved: {filename} to {folder}')
            else:
                print(f'no catagary for : {filename}')
if __name__=='__main__':
    organize_files()         
