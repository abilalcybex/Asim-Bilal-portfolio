import socket
import uuid

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_mac_address():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    return mac_address

if __name__ == '__main__':
    ip_address = get_ip_address()
    mac_address = get_mac_address()
    
    print(f"IP Address: {ip_address}")
    print(f"MAC Address: {mac_address}")
