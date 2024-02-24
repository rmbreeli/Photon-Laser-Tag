import socket

def receive_udp_broadcast(port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified port
    udp_socket.bind(('0.0.0.0', port))

    print(f"Listening for broadcasts on port {port}")

    try:
        while True:
            # Receive data and the address of the sender
            data, address = udp_socket.recvfrom(1024)
            
            # Print the received data and the sender's address
            print(f"Received from {address}: {data.decode()}")

    except KeyboardInterrupt:
        print("Stopping the UDP listener.")

    finally:
        # Close the socket
        udp_socket.close()

if __name__ == "__main__":
    port_to_listen = 7500

    receive_udp_broadcast(port_to_listen)