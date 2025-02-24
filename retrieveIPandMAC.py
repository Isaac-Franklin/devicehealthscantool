import socket
import uuid

def get_device_network_info():
    try:
        # Get the IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        # Get the MAC address
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> e) & 0xff)
                               for e in range(0, 8 * 6, 8)][::-1])
        
        return {
            "ip_address": ip_address,
            "mac_address": mac_address
        }

    except Exception as e:
        print(f"Error fetching network info: {e}")
        return {
            "ip_address": "N/A",
            "mac_address": "N/A"
        }
