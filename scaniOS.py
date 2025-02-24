import os

def get_installed_apps_iOS():
    apps_dir = "/Applications"
    apps = [app for app in os.listdir(apps_dir) if app.endswith(".app")]
    return apps

if __name__ == "__main__":
    installed_apps = get_installed_apps_iOS()
    print("Installed Applications:")
    for app in installed_apps:
        print(f"- {app}")


# find installed apps and date installed
import os
import subprocess
import datetime

def get_installed_apps():
    apps = []
    try:
        # Fetch list of applications using system_profiler
        result = subprocess.run(["system_profiler", "SPApplicationsDataType", "-json"], 
                                capture_output=True, text=True)
        output = result.stdout

        # Parse JSON output (requires Python 3.7+)
        import json
        data = json.loads(output)
        for app in data.get("SPApplicationsDataType", []):
            name = app.get("_name", "Unknown")
            path = app.get("path", "")
            installed_date = None

            # Attempt to fetch creation date of the app binary
            if path and os.path.exists(path):
                stat = os.stat(path)
                installed_date = datetime.datetime.fromtimestamp(stat.st_birthtime).date()

            apps.append({"name": name, "installed_date": installed_date})
    except Exception as e:
        print(f"Error fetching applications: {e}")
    return apps

# Example Usage
if __name__ == "__main__":
    apps = get_installed_apps()
    for app in apps:
        print(f"Name: {app['name']}, Installed Date: {app['installed_date']}")
