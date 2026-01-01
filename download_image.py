from bing_image_downloader import downloader
import os
import imghdr


# Download images
downloader.download(
    query="lion animal",
    limit=100,
    output_dir="lion_images",
    # adult_filter=True,
    force_replace=False,
    timeout=60
)

# Rename images from 1 to 100

folder_path = "lion_images/tiger animal"

files = os.listdir(folder_path)
files.sort()

for index, file in enumerate(files, start=1):
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join( f"{index}.jpg")

    os.rename(old_path, new_path)

print("✅ 100 cheetah images downloaded and renamed successfully.")

 
