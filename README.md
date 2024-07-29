# Digital Signature Project
This project demonstrates the use of RSA digital signatures in Python to ensure the authenticity and integrity of a message. It includes three main scripts: one for generating RSA keys, one for sending a signed message, and one for receiving and verifying the signature of the message.

## Project Structure:
keys.py: Generates and saves RSA public and private keys.
recipient.py: Receives and verifies the signed message.
sender.py: Signs and sends the message.

## Prerequisites
- Python 3.x
- rsa library
- socket library (part of Python standard library)
- hashlib library (part of Python standard library)
- json library (part of Python standard library)
- base64 library (part of Python standard library)
- os library (part of Python standard library)

``You can install the rsa library using pip:
pip install rsa 

## Usage
### Step 1: Generate RSA Keys
Run the keys.py script to generate a new pair of RSA keys. The public and private keys will be saved in the keys directory.

python keys.py

### Step 2: Start the Recipient (Server)
Run the recipient.py script to start the server, which listens for incoming messages and verifies their signatures.

python recipient.py

### Step 3: Send a Signed Message (Client)
Run the sender.py script to sign a message and send it to the server. You will be prompted to enter your message.

python sender.py

## How It Works
### Key Generation (keys.py)

1. Generates a pair of RSA keys (public and private).
2. Saves the keys in PEM format in the keys directory.

### Recipient (recipient.py)

1. Finds a free port and writes it to the config/config.json file.
2. Loads the public key from the keys directory.
3. Starts a socket server that listens for incoming connections.
4. Receives a message and its digital signature.
5. Verifies the signature using the public key and prints the result.

### Sender (sender.py)

1. Loads the private key from the keys directory.
2. Reads the port number from the config/config.json file.
3. Prompts the user to enter a message.
4. Hashes the message and creates a digital signature using the private key.
5. Sends the message and its signature to the recipient via a socket connection.

# Important Notes
This project is intended for educational purposes and should not be used in production environments without further enhancements and security considerations.
Ensure that the keys and config directories have appropriate permissions to prevent unauthorized access.


# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

# Contact
For any questions or suggestions, please contact me at [houaddad@gmail.com].