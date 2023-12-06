import requests
import socket

print("Helcome to RPC!\n")

ss = input("URL (www.example.com): ")
print("This will take some time...")
ports = range(1, 65535)

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ss, port))
    if result == 0:
        print(f"The port {port} is open. Making a GET request...")
        try:
            response = requests.get(f"https://{ss}:{port}", timeout=1)
            print(f"Port response {port}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred when making the request on the port {port}: {e}")
    sock.close()