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
        public_key_hex = public_key_hex[2:]
        public_bytes_from_hex = bytes.fromhex(public_key_hex)
        loaded_public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_bytes_from_hex)
    elif opt in ("-s", "--signature"):
        encoded_signature = arg
        signature = bytes.fromhex(encoded_signature)

if msg == "" or public_key_hex == "" or encoded_signature == "":
    print("All arguments are required!")
    print('./verify.py -m YOURMESSAGE -k PUBLIC-KEY-HEX -s SIGNATURE')
    sys.exit()

print("Message:\n", msg)
print("Signature:\n", encoded_signature)

# Verify
try:
    loaded_public_key.verify(signature, msg_as_bytes)
    print("Verified!")
except:
    print("Verification failed!")