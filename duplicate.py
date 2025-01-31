# from PIL import Image
# import imagehash
# import os

# def remove_duplicates(main_folder):
#     walker=os.walk(main_folder)
#     print(walker)
#     uniquefiles=dict()

#     for folder,sub_folders,files in walker:
#         for file in files:
#             filepath=os.path.join(folder,file)
#             image=Image.open(filepath)
#             image_hash=imagehash.dhash(image)
#             print(f" dhash value:{image_hash}")

#             if image_hash  in uniquefiles:
               
#                 os.remove(filepath)
#                 print(f"{filepath} has been deleted")
                
#             else:
#                 uniquefiles[image_hash]=filepath
            
# def main():
#     main_folder = r"Images"
#     if not os.path.exists(main_folder):
#         print(f"The folder {main_folder} does not exist.")
#         return
#     remove_duplicates(main_folder)

# if __name__ == "__main__":
#     main()
from PIL import Image
import imagehash
import os

def remove_duplicates(main_folder):
    # walker is a generator, so we need to iterate over it
    walker = os.walk(main_folder)
    
    # Iterating over walker to print directory structure
    for folder, sub_folders, files in walker:
        print(f"Folder: {folder}")
        print(f"Subfolders: {sub_folders}")
        print(f"Files: {files}")
        
        # Initialize a dictionary to track unique images based on hash
        uniquefiles = dict()

        for file in files:
            filepath = os.path.join(folder, file)
            
            # Open image and compute dhash
            image = Image.open(filepath)
            image_hash = imagehash.dhash(image)
            print(f" dhash value: {image_hash}")
            
            if image_hash in uniquefiles:
                # If hash is already in the dictionary, it's a duplicate, so delete the file
                os.remove(filepath)
                print(f"{filepath} has been deleted")
            else:
                # Otherwise, add the hash to the dictionary
                uniquefiles[image_hash] = filepath

# Specify the folder to check for duplicates
main_folder = r"Images"
remove_duplicates(main_folder)
