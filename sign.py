#!/usr/bin/env python3

import ecc_ed25519
import base64
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
signature = ecc_ed25519.get_signature_from_pem_file(msg_as_bytes, secret_key_path)
encoded_signature = signature.hex()

print("Your message:\n", msg)
print("Signature for your message:\n", encoded_signature)