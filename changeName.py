import os

def rename_mask_files(folder_path, old_prefix="annotated_", new_suffix="_mask.jpg"):

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    files = os.listdir(folder_path)

    for file_name in files:
        if file_name.startswith(old_prefix) and file_name.endswith(".jpg"):
            file_id = file_name[len(old_prefix):-4] 
            
            new_name = f"{file_id}{new_suffix}"

            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)
            print(f"Renamed: {file_name} -> {new_name}")
        else:
            print(f"Skipped: {file_name} (does not match format)")

folder_path = "C:/Users/jihye/OneDrive/문서/GitHub/Pytorch-UNet/data/masks"  
rename_mask_files(folder_path)
