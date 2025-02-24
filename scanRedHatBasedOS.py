import subprocess

def get_installed_apps_redHat():
    try:
        output = subprocess.check_output(["rpm", "-qa"], text=True)
        apps = output.splitlines()
        return apps
    except FileNotFoundError:
        return ["rpm command not found. Is this a RedHat-based system?"]

if __name__ == "__main__":
    installed_apps = get_installed_apps_redHat()
    print("Installed Applications:")
    for app in installed_apps:
        print(f"- {app}")




# find all installed and dates installed
import os
import datetime

def get_file_creation_date(filepath):
    try:
        stat = os.stat(filepath)
        if hasattr(stat, "st_birthtime"):  # macOS and Windows
            return datetime.datetime.fromtimestamp(stat.st_birthtime).date()
        else:  # Linux (fallback to last modified date)
            return datetime.datetime.fromtimestamp(stat.st_mtime).date()
    except Exception as e:
        print(f"Error fetching date for {filepath}: {e}")
        return None
