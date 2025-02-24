import os
import psutil
import platform
from datetime import datetime

from getDeviceLocation import get_device_location
from retrieveIPandMAC import get_device_network_info

def get_device_health_location_info():
    # Device Information
    device_info = {
        "Device Name": platform.node(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "CPU Cores": psutil.cpu_count(logical=True),
        "RAM Size (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
    }
    
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Memory Usage
    memory = psutil.virtual_memory()
    memory_usage = {
        "Total Memory (GB)": round(memory.total / (1024 ** 3), 2),
        "Used Memory (GB)": round(memory.used / (1024 ** 3), 2),
        "Memory Usage (%)": memory.percent
    }
    
    # Disk Usage
    disk = psutil.disk_usage('/')
    disk_usage = {
        "Total Disk (GB)": round(disk.total / (1024 ** 3), 2),
        "Used Disk (GB)": round(disk.used / (1024 ** 3), 2),
        "Disk Usage (%)": disk.percent
    }
    
    # Battery Status (for laptops)
    battery = psutil.sensors_battery()
    battery_status = {
        "Battery Percentage": battery.percent if battery else "N/A",
        "Charging": battery.power_plugged if battery else "N/A"
    }
    
    # System Uptime
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    system_uptime = str(uptime).split('.')[0]  # Format uptime
    getDeviceNetworkInfo = get_device_network_info()
    deviceIPAddress = getDeviceNetworkInfo['ip_address']                  
    deviceMacAddress = getDeviceNetworkInfo['mac_address']
    
    # get location data
    deviceLocationData = get_device_location()
    print(deviceLocationData)
    
    try:
        deviceLocationCountry = deviceLocationData['Country']
        deviceLocationRegion = deviceLocationData['Region']
        deviceLocationCity = deviceLocationData['City']
        deviceLocationLatitude = deviceLocationData['Latitude']
        deviceLocationLongitude = deviceLocationData['Longitude']
        deviceLocationISP = deviceLocationData['ISP']
    except:
        deviceLocationCountry = 'Not Found: Bad Connection'
        deviceLocationRegion = 'Not Found: Bad Connection'
        deviceLocationCity = 'Not Found: Bad Connection'
        deviceLocationLatitude = 'Not Found: Bad Connection'
        deviceLocationLongitude = 'Not Found: Bad Connection'
        deviceLocationISP = 'Not Found: Bad Connection'

    # Combine All Data
    health_location_status = {
        "deviceLocationCountry":deviceLocationCountry,
        "deviceLocationRegion":deviceLocationRegion,
        "deviceLocationCity":deviceLocationCity,
        "deviceLocationLatitude":deviceLocationLatitude,
        "deviceLocationLongitude":deviceLocationLongitude,
        "deviceLocationISP":deviceLocationISP,
        "deviceIPAddress":deviceIPAddress,
        "deviceMacAddress":deviceMacAddress,
        "Device Info": device_info,
        "CPU Usage (%)": cpu_usage,
        "Memory Usage": memory_usage,
        "Disk Usage": disk_usage,
        "Battery Status": battery_status,
        "System Uptime": system_uptime
    }
    
    print('health_location_status')
    print(health_location_status)
    return health_location_status

# # Fetch and Print Health Data
# if __name__ == "__main__":
#     health_data = get_device_info()
#     for key, value in health_data.items():
#         print(f"{key}: {value}")
