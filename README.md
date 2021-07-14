# Ed25519-sign-and-verify

Helper scripts to sign a given message by using an ed25519 secret key (PEM) file, and then to verify the signed message by using the public key in hex format.

## Prerequisites
A GNU/Linux environment with Python 3 and git.

## Installation

On Ubuntu 20.04:
`sudo apt update && sudo apt install git && git clone https://github.com/mrkara/Ed25519-sign-and-verify.git`

## Usage

First, get into the clone directory:

`cd Ed25519-sign-and-verify`

Then;

* To sign:

  `./sign -m YOURMESSAGE -k PATH-TO-YOUR-SECRET-KEY.pem`

* To verify:

  `./verify -m YOURMESSAGE -k YOUR-PUBLIC-KEY-HEX -s SIGNATURE-IN-BASE-64-FORMAT`

## Credits
* Uses the [ecc_ed25519.py](https://github.com/momipsl/pycspr/blob/main/pycspr/crypto/ecc_ed25519.py) module from [pycspr](https://github.com/momipsl/pycspr)
