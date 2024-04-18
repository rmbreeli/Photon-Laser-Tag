import socket

def broadcast_message():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Use your subnet's broadcast address here
    broadcast_address = '127.0.0.1'  # Example for a common home network
    port = 7501
    
    message = "1:2"
    
    try:
        sock.sendto(message.encode(), (broadcast_address, port))
        print("Message broadcasted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()

broadcast_message()
