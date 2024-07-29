import rsa
import os

os.makedirs('keys', exist_ok=True)

(public_key, private_key) = rsa.newkeys(2048)

#To save the public key
with open('keys/public_key.pem', 'wb') as file:
    file.write(public_key.save_pkcs1('PEM'))

#To save the private key
with open('keys/private_key.pem', 'wb') as file:
    file.write(private_key.save_pkcs1('PEM'))

print("Public and private keys generated and saved in 'keys' directory.")
