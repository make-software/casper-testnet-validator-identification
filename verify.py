#!/usr/bin/env python3

import ecc_ed25519
import sys, getopt
from cryptography.hazmat.primitives.asymmetric import ed25519

msg = ""
public_key_hex = ""
encoded_signature = ""

try:
    opts, args = getopt.getopt(sys.argv[1:],"hm:k:s:",["message=","publickeyhex=", "signature="])
except getopt.GetoptError:
    print('verify.py -m YOURMESSAGE -k PUBLIC-KEY-HEX -s SIGNATURE')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('verify.py -m YOURMESSAGE -k PUBLIC-KEY-HEX -s SIGNATURE')
        sys.exit()
    elif opt in ("-m", "--message"):
        msg = arg
        msg_as_bytes = str.encode(msg)
    elif opt in ("-k", "--publickeyhex"):
        public_key_hex = arg
        # Get rid of the prefix 01
        public_bytes_from_hex = bytes.fromhex(public_key_hex[2:])
        loaded_public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_bytes_from_hex)
    elif opt in ("-s", "--signature"):
        encoded_signature = arg
        signature = bytes.fromhex(encoded_signature)

if msg == "" or encoded_signature == "":
    print("Message and signature are required!")
    print('./verify.py -m YOURMESSAGE -k PUBLIC-KEY-HEX -s SIGNATURE')
    sys.exit()

# Read the public_key_hex from default location if not given as param
if public_key_hex == "":
    public_key_hex_location = "/etc/casper/validator_keys/public_key_hex"
    with open(public_key_hex_location, 'r') as fstream:
        public_key_hex = fstream.readlines()[0]
        # Get rid of the prefix
        public_bytes_from_hex = bytes.fromhex(public_key_hex[2:])
        loaded_public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_bytes_from_hex)

print("Public Key:\n", public_key_hex)
print("Message:\n", msg)
print("Signature:\n", encoded_signature)

# Verify
try:
    loaded_public_key.verify(signature, msg_as_bytes)
    print("Verified!")
except:
    print("Verification failed!")