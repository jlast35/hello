#! /usr/bin/env bash

# first of all, you have to derive a PEM format public key 
# from your private RSA key if you haven't already.
[ -e ~/.ssh/id_rsa.pub.pem ] \
|| openssl rsa -in ~/.ssh/id_rsa -pubout > ~/.ssh/id_rsa.pub.pem

echo 'Creating plain.txt'
# create a plain text file
echo 'Hello Encryption!' > plain.txt

echo 'Creating encrypted.txt'
# encrypt plain.txt using your public key and save it to encrypted.txt
cat plain.txt \
| openssl rsautl -encrypt -pubin -inkey ~/.ssh/id_rsa.pub.pem \
> encrypted.txt

# Alternative method:
# openssl rsautl -encrypt -inkey ~/.ssh/id_rsa.pub.pem -pubin -in plain.txt -out encrypted.txt

echo 'Creating decrypted.txt'
# decrypt encrypted.txt using your private key and save it to decrypted.txt
cat encrypted.txt \
| openssl rsautl -decrypt -inkey ~/.ssh/id_rsa \
> decrypted.txt

# Alternative method:
# openssl rsautl -decrypt -inkey ~/.ssh/id_rsa -in encrypted.txt

echo 'Done.'
exit 0

