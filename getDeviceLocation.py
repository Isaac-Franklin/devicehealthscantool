import requests

def get_device_location():
    try:
        # Step 1: Get the public IP address
        ip_response = requests.get("https://api.ipify.org?format=json")
        public_ip = ip_response.json().get("ip")

        # Step 2: Use the IP to fetch location data
        location_response = requests.get(f"http://ip-api.com/json/{public_ip}")
        location_data = location_response.json()

        if location_data['status'] == 'success':
            device_location = {
                "IP Address": public_ip,
                "Country": location_data.get("country"),
                "Region": location_data.get("regionName"),
                "City": location_data.get("city"),
                "Latitude": location_data.get("lat"),
                "Longitude": location_data.get("lon"),
                "ISP": location_data.get("isp")
            }
            return device_location
        else:
            return {"Error": "Could not determine location"}
    except Exception as e:
        return {"Error": str(e)}
