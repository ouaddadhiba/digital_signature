import rsa
import hashlib
import json
import base64
import socket

# Load the config file
with open('config/config.json', 'r') as file:
    config = json.load(file)

PORT = config['port']
HOST = '127.0.0.1'

# Load the private key
with open('keys/private_key.pem', 'rb') as file:
    private_key = rsa.PrivateKey.load_pkcs1(file.read())

# Create and connect the client socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_sock.connect((HOST, PORT))
    
    # Input message from the user
    msg = input(f"Your message: ")
    message = msg.encode('utf-8')
    
    #To hash the message
    hash_message = hashlib.sha256(message).digest()
    print("Hashed message: ", hash_message)
    
    # Create a digital Signature
    signature = rsa.sign(hash_message, private_key, 'SHA-256')
    print("Signature: ", signature)

    # Serialize the message and signature into a JSON-compatible format
    data = {
        'real_message' : msg,
        'signature': base64.b64encode(signature).decode('utf-8') # Converting the signature to base64 for JSON compatibility
    }

    json_str = json.dumps(data)

    # Send the serialized data to the server
    client_sock.sendall(json_str.encode('utf-8'))

finally:
    # Close the connection
    client_sock.close()