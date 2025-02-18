import os
import re
from pathlib import Path
import shutil

# Define the working directory and navigate to it
base_dir = Path("C:/Users/ezeki/Videos/Movies")
os.chdir(base_dir)
print(f"Working in: {base_dir}")

# Create the target folder
folder_path = base_dir / "The Lincoln Lawyer Season 2"
folder_path.mkdir(exist_ok=True)
print(f"Created/Verified folder: {folder_path}")

# Process files in the directory
for file in base_dir.iterdir():
    if file.is_dir():
        continue  # Skip directories

    # Move files that start with "The Lincoln Lawyer"
    if file.name.casefold().startswith("the lincoln lawyer"):
        print(f"Moving: {file.name}")
        try:
            shutil.move(str(file), str(folder_path / file.name))
        except Exception as e:
            print(f"Error moving {file.name}: {e}")

    # Rename files that start with "tfpdl"
    elif file.name.casefold().startswith("tfpdl"):
        name, ext = os.path.splitext(file.name)
        parts = [s.strip() for s in name.split("-")]

        # Ensure we have enough parts to rename
        if len(parts) > 1:
            new_name = f"{parts[1]}{ext}"
            new_name = re.sub(r'tlnclwy\S*?', 'The Lincoln Lawyer ', new_name)
            new_name = re.sub(r'20\S*?', 'S2_E', new_name)
            new_name = re.sub(r'72x\S*?', '_720p', new_name)

            new_path = file.with_name(new_name)

            # Rename safely
            if new_path.exists():
                print(f"Skipping rename (file already exists): {new_name}")
            else:
                print(f"Renaming: {file.name} -> {new_name}")
                try:
                    file.rename(new_path)
                except Exception as e:
                    print(f"Error renaming {file.name}: {e}")

print("Processing complete.")
