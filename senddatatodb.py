import requests
import platform
import json

def saveAppsToDB(applications, deviceHealthInfo):
    print('Save to apps to DB function called')
    
    # Sending data to Django backend
    url = "https://dhms.itservicedeskafrica.com/scandevice/"
    # url = "http://127.0.0.1:5000/scandevice/"

    payload = {
        "applications": json.dumps(applications),
        "deviceHealthInfo": json.dumps(deviceHealthInfo),
    }

    response = requests.post(url, data=payload)

    if response.status_code == 201:
        print("Applications saved successfully")
    else:
        print(f"Failed to save applications: {response.status_code}")

if __name__ == "__main__":
    saveAppsToDB()


# def saveDeviceHealthData(applications):
#     print('Save to apps to DB function called')
    
#     # Sending data to Django backend
#     # url = "https://dhms.itservicedeskafrica.com/scandevice/"
#     url = "http://127.0.0.1:5000/scandevice/"
#     device_name = platform.node()  # Get the device's hostname

#     payload = {
#         "applications": json.dumps(applications),
#         "device_name": device_name
#     }

#     response = requests.post(url, data=payload)

#     if response.status_code == 201:
#         print("Applications saved successfully")
#     else:
#         print(f"Failed to save applications: {response.status_code}")

# if __name__ == "__main__":
#     saveDeviceHealthData()
