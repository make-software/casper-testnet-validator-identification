# casper-testnet-validator-identification

Helper scripts to sign a given message by using the validator secret key (ed25519 algorithm) (PEM) file, and then to verify the signed message by using the public key in hex format.

## Prerequisites
`Python 3`, `git` and the `cryptography` library of Python are needed on your node with a GNU/Linux environment (preferably Ubuntu 20.04.)

Install them by issuing the following commands:

`sudo apt update && sudo apt install git`

`pip install cryptography`

## Installation

Go to your home directory:

`cd ~`

Clone the repository:

`git clone https://github.com/make-software/casper-testnet-validator-identification.git`

## Instructions

Move to your home directory (or the directory where you cloned/installed the repo in the installation step):

`cd ~`

Enter the clone directory:

`cd casper-testnet-validator-identification`

Sign your email address with your secret key:

`sudo -u casper ./sign.py -m YOUR-EMAIL-ADDRESS`

You will get an output similar to this:

```bash
Public Key:
 0118157c4c169d3534742084bfca4b891606958a96dc46f54444f0a790ef096d28
Message:
 me@mydomain.com
Signature:
 fcb9216b98e589686633df826af4d37839f67ea12dbf09264db346d0e6cf0a1725a7aedba7d824498e2e0cf83e3d461ac0257ad204f3f3229c2f184d86295706
 ```

 **Copy and paste the signature to the Casper Testnet Public Key and Email Verification form.**

### Optional

You can verify your signature before submitting it via the provided form to make sure there are no errors.

Issue this command to verify your signature:

  `./verify.py -m YOUR-EMAIL-ADDRESS -s SIGNATURE`

You should get an output similar to this:

```bash
Public Key:
 0118157c4c169d3534742084bfca4b891606958a96dc46f54444f0a790ef096d28
Message:
 me@mydomain.com
Signature:
 fcb9216b98e589686633df826af4d37839f67ea12dbf09264db346d0e6cf0a1725a7aedba7d824498e2e0cf83e3d461ac0257ad204f3f3229c2f184d86295706
Verified!
```

## Credits
* Uses the [ecc_ed25519.py](https://github.com/momipsl/pycspr/blob/main/pycspr/crypto/ecc_ed25519.py) module from [pycspr](https://github.com/momipsl/pycspr)
