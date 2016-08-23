#requires "pip install paramiko"  - which installs pycrypto as one of its dependecies
#which for Windows requires the same visual C++ compiler your Python version was installed with
#which for Python 2.7 can be found here:
#http://www.microsoft.com/en-us/download/details.aspx?id=44266


from Crypto.Cipher import AES
#base64 is used for encoding. dont confuse encoding with encryption#
#encryption is used for disguising data
#encoding is used for putting data in a specific format
import base64
# os is for urandom, which is an accepted producer of randomness that
# is suitable for cryptology.
import os

def encrypt(privateInfo):

    #32 bytes = 256 bits
    #16 = 128 bits
    # the block size for cipher obj, can be 16 24 or 32. 16 matches 128 bit.
    BLOCK_SIZE = 16

    # the character used for padding
    # used to ensure that your value is always a multiple of BLOCK_SIZE
    PADDING = '{'

    # function to pad the functions. Lambda
    # is used for abstraction of functions.
    # basically, its a function, and you define it, followed by the param
    # followed by a colon,
    # ex = lambda x: x+5
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

    # encrypt with AES, encode with base64
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    # generate a randomized secret key with urandom
    secret = os.urandom(BLOCK_SIZE)
    print 'Encryption key:', ":".join("{:02x}".format(ord(c)) for c in secret)

    # creates the cipher obj using the key
    cipher = AES.new(secret)

    # encodes you private info!
    encryptedString = EncodeAES(cipher, privateInfo)
    print 'Encrypted string:', ":".join("{:02x}".format(ord(c)) for c in encryptedString)
    return encryptedString, secret


def decrypt(encryptedString, secret):

    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    #Key is FROM the printout of 'secret' in encryption
    #below is the encryption.
    encryption = encryptedString
    key = secret
    cipher = AES.new(key)
    decryptedString = DecodeAES(cipher, encryptedString)
    return decryptedString


#print crypt.encrypt('Hello World')
print decrypt(*encrypt('Hello World'))
exit()
