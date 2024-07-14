import socket
import json
import multiprocessing

def handle_client(conn, addr, processing=False):
    # print(f"Connected by {addr}")
    pyIPAddress, pyPort = addr
    while True:
        # If a request is already being processed, wait for it to finish
        if processing:
            continue

        # Receive the filename from the client
        data = conn.recv(1024)

        # If no data was received, break out of the loop
        if not data:
            break

        # Extract the JSON data from the filename
        json_data = data[data.find(b"{"):]

        # Set the processing flag to True
        processing = True

        # Convert the JSON data to a Python dictionary
        try:
            data = json.loads(json_data.decode())
        except json.JSONDecodeError:
            print("Error: Invalid JSON data received from client")
            processing = False
            continue

        # Print the data received from the client
        pyWS = data["ws"]
        pyTemperature = data["temperature"]
        pyHumidity = data["humidity"]

        # print("Weather station number:", data["ws"])
        # print("Temperature:", data["temperature"])
        # print("Humidity:", data["humidity"])

        if "rain" in data:
            rain = data["rain"]
            pyRain = rain
            # print("Rain:", rain)
        else:
            # print("Rain: N/A")
            pyRain = "N/A"

        if "pressure" in data:
            pressure = data["pressure"]
            pyPressure = pressure
            # print("Pressure:", pressure)
        else:
            # print("Pressure: N/A")
            pyPressure = "N/A"

        print("Connected to IP Address: " + str(pyIPAddress) + " | Port: " + str(pyPort) + "\n" +
              "Weather station number:" + str(pyWS) + "\n" +
              "Temperature: " + str(pyTemperature)+ "\n"+
              "Humidity: " + str(pyHumidity) + "\n" +
              "Rain: " + str(pyRain) + "\n" +
              "Pressure: " + str(pyPressure) + "\n")

        # Set the processing flag to False
        processing = False

    # Close the socket
    conn.close()

def main():
    # Prompt the user to enter the IP address and port number
    ip_address = input("Enter the IP address to listen on: ")
    port = int(input("Enter the port number to listen on: "))

    # Set the IP address and port number to listen on
   #  ip_address = "192.168.3.189"
   #  port = 9001

    # Create a socket object and bind it to the IP address and port number
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_address, port))

    # Set the maximum number of connections to queue up
    s.listen(5)

    # Start a loop to handle incoming connections
    while True:
        # Accept an incoming connection and create a new process to handle it
        conn, addr = s.accept()
        p = multiprocessing.Process(target=handle_client, args=(conn, addr))

        # Start the process to handle the connection
        p.start()

if __name__ == '__main__':
    # Call the main function if the script is being run as the main program
    main()