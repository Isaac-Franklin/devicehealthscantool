import subprocess

def get_installed_apps_ubuntu():
    try:
        output = subprocess.check_output(["dpkg", "--get-selections"], text=True)
        apps = [line.split("\t")[0] for line in output.splitlines()]
        return apps
    except FileNotFoundError:
        return ["dpkg command not found. Is this a Debian-based system?"]

if __name__ == "__main__":
    installed_apps = get_installed_apps_ubuntu()
    print("Installed Applications:")
    for app in installed_apps:
        print(f"- {app}")


# find installed apps and dates
import subprocess
import datetime

def get_installed_apps():
    apps = []
    try:
        # Run dpkg command to list packages and installation dates
        result = subprocess.run(
            ["dpkg-query", "-W", "-f=${Package} ${Version} ${Installed-Size} ${Date}\\n"],
            capture_output=True, text=True
        )
        output = result.stdout
        for line in output.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                name = parts[0]
                installed_date = None  # `dpkg` doesn't directly provide installation dates.
                apps.append({"name": name, "installed_date": installed_date})
    except Exception as e:
        print(f"Error fetching applications: {e}")
    return apps

# Example Usage
if __name__ == "__main__":
    apps = get_installed_apps()
    for app in apps:
        print(f"Name: {app['name']}, Installed Date: {app['installed_date']}")
