import rsa
import hashlib
import socket
import json
import os
import base64


# Function to find the free ports to use
def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

#Configuration
HOST = '127.0.0.1'
PORT = find_free_port()

# Create config directory if it doesn't exist
os.makedirs('config', exist_ok=True)

# Create and write to the config file
with open('config/config.json', 'w') as config_file:
    json.dump({'port': PORT}, config_file)

# Load the public key
with open('keys/public_key.pem', 'rb') as key_file:
    public_key = rsa.PublicKey.load_pkcs1(key_file.read())

# Create and bind the server socket 
server_sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((HOST, PORT))
server_sock.listen(1) 

print(f"Server listening on {HOST}:{PORT}")

try:
    #Accept a connection
    communication_sock, addr = server_sock.accept()
    print(f"Connection accepted from {addr}")

    msg_data = communication_sock.recv(1024).decode('utf-8')

    # Deserialize JSON data
    received_data = json.loads(msg_data)
    signature = received_data['signature']
    message = received_data['real_message']
   
    # Verify the singature
    message_bytes = message.encode('utf-8')
    signature = base64.b64decode(signature)
    hash_message = hashlib.sha256(message_bytes).digest()
    
    try:
        rsa.verify(hash_message, signature, public_key)
        print("Signature is verified!")
    except rsa.VerificationError:
        print("Verification Failed!")

finally:
    communication_sock.close()
    server_sock.close()
