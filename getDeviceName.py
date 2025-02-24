import socket

def get_device_name():
    try:
        # Retrieve the hostname of the device
        device_name = socket.gethostname()
        return device_name
    except Exception as e:
        print(f"Error fetching device name: {e}")
        return "N/A"

# Example usage
if __name__ == "__main__":
    device_name = get_device_name()
    print(f"Device Name: {device_name}")
