import hashlib
import os
import string
import random

def hash_preimage(target_string):
    k = 10
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'
    
    while True:
    y = os.urandom(64)
    wy = hashlib.sha256(y)
    ybits = ''.join(format(byte, '08b') for byte in wy.digest())
    if target_string[-k:] == ybits[-k:]:
        break

    return( ybits )
