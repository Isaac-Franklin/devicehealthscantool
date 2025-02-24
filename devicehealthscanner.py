# pyinstaller --onefile --icon=itsalogo.ico --noconsole devicehealthscanner.py

import sys
from addToStartupRegistry import add_to_startup
from findDeviceHealthParameters import get_device_health_location_info
from retrieveIPandMAC import get_device_network_info
from scanRedHatBasedOS import get_installed_apps_redHat
from scanUbuntu import get_installed_apps_ubuntu
from scanWindows import get_installed_apps, get_installed_apps_wind
from scaniOS import get_installed_apps_iOS
from senddatatodb import saveAppsToDB
import os

# add app to device start up folder
def is_first_run():
    return not os.path.exists(os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup', 'deviceappscanner.exe'))

# add app to device start up folder (only on first run)
if is_first_run():
    add_to_startup()

    
def check_platform():
    platform = sys.platform
    if platform.startswith("win"):
        installed_apps = get_installed_apps()
        InstalledAppsAndDate = get_installed_apps_wind()
        print(InstalledAppsAndDate)
        findDeviceHealthStatus = get_device_health_location_info()
        saveAppsToDB(InstalledAppsAndDate, findDeviceHealthStatus)
        print("Windows Applications Found")
        print('findDeviceHealthStatus')
        print(findDeviceHealthStatus)
        
    elif platform.startswith("darwin"):
        print("Running on macOS")
        installed_apps = get_installed_apps_iOS()
        print("Installed Applications:")
        for app in installed_apps:
            print(f"- {app}")
        
    elif platform.startswith("linux"):
        print("Running on Linux")
        installed_apps = get_installed_apps_ubuntu()
        print("Installed Applications:")
        for app in installed_apps:
            print(f"- {app}")
        
    else:
        print("Unsupported platform")
        installed_apps = get_installed_apps_redHat()
        print("Installed Applications:")
        for app in installed_apps:
            print(f"- {app}")
        

if __name__ == "__main__":
    check_platform()



# itsalogo.png
# pyinstaller --onefile --icon=static\images\itsalogo.png checkSystem.py
# pyinstaller --onefile --noconsole checkSystem.py
# pyinstaller --onefile --name="AppChecker" checkSystem.py


# SCAN FOR DEVICE HEALTH AND SEND DATA TO DB

# import requests

# def send_to_backend(health_data):
#     url = "http://your-django-api-url.com/save-device-health"
#     payload = get_device_health_info()

#     try:
#         response = requests.post(url, json=payload)
#         if response.status_code == 200:
#             print("Data sent successfully.")
#         else:
#             print("Failed to send data:", response.json())
#     except Exception as e:
#         print("Error sending data to server:", str(e))

