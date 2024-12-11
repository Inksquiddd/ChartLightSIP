import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Host on all interfaces, port 12345
server_socket.listen(1)
print("Waiting for a connection...")

# Wait for a connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        # Receive text data from the client        
        # Input a response and send it to the client
        response = input("You: ")
        conn.sendall(response.encode('utf-8'))
except KeyboardInterrupt:
    print("Server stopped.")
finally:
    conn.close()
    server_socket.close()
