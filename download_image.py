from bing_image_downloader import downloader
import os
import imghdr


# Download images
# downloader.download(
#     query="lion animal",
#     limit=100,
#     output_dir="lion_images",
#     # adult_filter=True,
#     force_replace=False,
#     timeout=60
# )

# Rename images from 1 to 100

folder_path = "Images/Tiger"

files = os.listdir(folder_path)
files.sort()
c = 162
for index, file in enumerate(files, start=1):
    old_path = os.path.join(folder_path, file)
    ext = old_path.split('.')[-1].lower()

    new_path = os.path.join(f"{c}.jpg") if ext != "txt" else os.path.join(f"{c}.txt")
    if index % 2 == 0:
        c += 1
    print(f"Renaming {old_path} to {new_path}")
    os.rename(old_path, new_path)


print("✅ 100 cheetah images downloaded and renamed successfully.")
