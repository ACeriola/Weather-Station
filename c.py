import socket
import os

# Define a function to send a JSON file to a server
def send_file(json_data, ip_address, port):
    # Print the JSON data
    print(json_data)

    # Create a socket object and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))

    # Send the JSON data to the server
    s.sendall(json_data)

    # Close the socket
    s.close()

def main():
    # Prompt the user to enter the IP address and port number
    ip_address = input("Enter the IP address to send the json files to: ")
    port = int(input("Enter the port number to send the json files to: "))

    # Loop through all JSON files in the 'json_files' directory
    for filename in os.listdir('json_files'):
        if filename.endswith('.json'):
            # Read the contents of the JSON file
            with open(os.path.join('json_files', filename), 'rb') as f:
                json_data = f.read()

            # Send the JSON data to the server using the send_file function
            send_file(json_data, ip_address, port)

if __name__ == '__main__':
    # Call the main function if the script is being run as the main program
    main()