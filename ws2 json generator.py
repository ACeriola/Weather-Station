import socket
import json
import random
import time

# Define the IP address and port number
ip_address = "192.168.3.189"
port = 9001

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((ip_address, port))

# Generate and send a random JSON object every second
while True:
    # Generate a random JSON object
    data = {
        "ws": 2,
        "temperature": round(random.uniform(20.0, 30.0), 1),
        "humidity": random.randint(60, 70)
    }
    json_data = json.dumps(data)

    # Send the JSON data to the server
    s.sendall(json_data.encode())

    # Print the JSON data
    print(json_data)

    # Wait for one second before generating and sending the next JSON object
    time.sleep(0.25)

# Close the socket
s.close()