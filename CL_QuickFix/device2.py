import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Replace with the server's IP address
    server_ip = '192.168.1.100'  # Example: Replace with your server's IP
    server_port = 12345

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")

    # Send a message
    message = "Hello, World!"
    client_socket.send(message.encode('utf-8'))
    print(f"Sent to server: {message}")

    # Receive a response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
