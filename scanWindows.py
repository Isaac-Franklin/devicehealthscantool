import winreg

from getDeviceName import get_device_name
from retrieveIPandMAC import get_device_network_info

def get_installed_apps():
    print('file called')
    apps = []
    uninstall_keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    
    for key_path in uninstall_keys:
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
            for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
                try:
                    sub_key_name = winreg.EnumKey(reg_key, i)
                    sub_key = winreg.OpenKey(reg_key, sub_key_name)
                    app_name, _ = winreg.QueryValueEx(sub_key, "DisplayName")
                    apps.append(app_name)
                except FileNotFoundError:
                    pass
                except OSError:
                    pass
        except FileNotFoundError:
            pass
    return apps

if __name__ == "__main__":
    installed_apps = get_installed_apps()
    print("Installed Applications:")
    for app in installed_apps:
        print(f"- {app}")



# get apps and date installed
import winreg
from datetime import datetime, date

def get_installed_apps_wind():
    apps = []
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",   # 64-bit programs
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"  # 32-bit programs
    ]

    for reg_path in registry_paths:
        try:
            registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            key = winreg.OpenKey(registry, reg_path)

            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                try:
                    name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    install_date = winreg.QueryValueEx(subkey, "InstallDate")[0]                    
                    getDeviceNetworkInfo = get_device_network_info()
                    deviceIPAddress = getDeviceNetworkInfo['ip_address']                  
                    deviceMacAddress = getDeviceNetworkInfo['mac_address']
                    deviceName = get_device_name()
                    # Convert InstallDate (YYYYMMDD) to a readable format
                    if install_date.isdigit() and len(install_date) == 8:
                        install_date_obj = datetime.strptime(install_date, "%Y%m%d").date()
                        formatted_date = install_date_obj.strftime("%Y-%m-%d")
                    else:
                        formatted_date = "N/A"

                    apps.append({
                        "name": name, 
                        "installed_date": formatted_date, 
                        'deviceIPAddress':deviceIPAddress, 
                        'deviceMacAddress':deviceMacAddress,
                        'deviceName':deviceName
                        })
                    
                except FileNotFoundError:
                    continue
                except Exception as e:
                    print(f"Error reading subkey: {e}")
                finally:
                    winreg.CloseKey(subkey)
        except Exception as e:
            print(f"Error accessing registry path {reg_path}: {e}")
        finally:
            winreg.CloseKey(key)
    print('get_installed_apps_wind RAN')

    return apps
