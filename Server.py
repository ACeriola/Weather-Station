import socket
import json
import multiprocessing
import time

def handle_client(data, processing=False):
    # print(f"Connected by {addr}")
    pyIPAddress = '192.168.127.1'
    pyPort = 80
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
        pyTime = data["Time"]
        pyStation = data["Station"]
        pyTemperature = data["Temperature"]
        pyHumidity = data["Humidity"]
        pyHeatIndex = data["HeatIndex"]
        pyPressure = data["Pressure"]
        pyAltitude = data["Altitude"]
        pyRaining = data["Raining"]

        # print("Weather station number:", data["ws"])
        # print("Temperature:", data["temperature"])
        # print("Humidity:", data["humidity"])

        # if "rain" in data:
        #     rain = data["rain"]
        #     pyRain = rain
            # print("Rain:", rain)
        # else:
            # print("Rain: N/A")
        #     pyRain = "N/A"

        # if "pressure" in data:
        #     pressure = data["pressure"]
        #     pyPressure = pressure
            # print("Pressure:", pressure)
        # else:
            # print("Pressure: N/A")
        #     pyPressure = "N/A"

        print("Connected to IP Address: " + str(pyIPAddress) + " | Port: " + str(pyPort) + "\n" +
              "Time:" + str(pyStation) + "\n" +
              "Weather station number:" + str(pyStation) + "\n" +
              "Temperature: " + str(pyTemperature)+ "\n"+
              "Humidity: " + str(pyHumidity) + "\n" +
              "Heat Index: " + str(pyHeatIndex) + "\n" +
              "Pressure: " + str(pyPressure) + "\n" +
              "Altitude: " + str(pyAltitude) + "\n" +
              "Raining: " + str(pyRaining) + "\n")

        # Set the processing flag to False
        processing = False

    # Close the socket
    conn.close()

def connect_client():
   # Prompt the user to enter the IP address and port number
    ip_address = '192.168.127.1'
    port = 80

    # Create a socket object and bind it to the IP address and port number

    # Set the maximum number of connections to queue up
    # s.listen(5)

    # Start a loop to handle incoming connections
    while True:
      # Accept an incoming connection and create a new process to handle it
      # conn, addr = s.accept()
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip_address, port))
      s.send(b'hello ESP32')
      data = b''
      print(data)
      try:
        data += s.recv(1024)
      except:
        data = b'except'
      print(data)
      s.close()

def main():
    
      p = multiprocessing.Process(target=connect_client)

      # Start the process to handle the connection
      p.start()

if __name__ == '__main__':
    # Call the main function if the script is being run as the main program
    main()
