import os
import sys
import shutil

def add_to_startup():
    # Use sys.argv[0] to get the path of the executable
    exe_path = os.path.abspath(sys.argv[0])

    # Get the Startup folder path
    startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')

    # Name of the executable
    exe_name = os.path.basename(exe_path)

    # Target path in the Startup folder
    target_path = os.path.join(startup_folder, exe_name)

    # Copy the executable to the Startup folder
    if not os.path.exists(target_path):
        shutil.copy(exe_path, target_path)
        print(f"{exe_name} added to startup successfully.")
    else:
        print(f"{exe_name} is already in the Startup folder.")

# Run this function
add_to_startup()
