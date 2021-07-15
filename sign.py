#!/usr/bin/env python3

import ecc_ed25519
import sys, getopt

msg = ""
secret_key_path = "/etc/casper/validator_keys/secret_key.pem"

try:
    opts, args = getopt.getopt(sys.argv[1:],"hm:k:",["message=","secretkey="])
except getopt.GetoptError:
    print('sign.py -m YOURMESSAGE -k PATH-TO-YOUR-SECRET-KEY')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('sign.py -m YOURMESSAGE -k PATH-TO-YOUR-SECRET-KEY')
        sys.exit()
    elif opt in ("-m", "--message"):
        msg = arg
    elif opt in ("-k", "--secretkey"):
        secret_key_path = arg

if msg == "":
    print("Message can't be empty!")
    sys.exit()

msg_as_bytes = str.encode(msg)

try:
    signature = ecc_ed25519.get_signature_from_pem_file(msg_as_bytes, secret_key_path)
except FileNotFoundError:
    print("ERROR: Couldn't access your private key at this location: ", secret_key_path)
    print("Please make sure your secret_key.pem file is at the given location and is accessible by the current user.")
    print("If you have your key at a different location, you can define its path by using the -k parameter.")
    print("Usage: sign.py -m YOURMESSAGE -k PATH-TO-YOUR-SECRET-KEY")
    sys.exit()

encoded_signature = signature.hex()

print("Message:\n", msg)
print("Signature:\n", encoded_signature)