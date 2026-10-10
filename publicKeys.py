""" 
RSA encryption is a modular exponentiation 
of a message with an exponent 'e' and a modulus 'N'
which is the product of two primes: 'p' and 'q'

The exponent and the modulus form the public key of RSA

THE MOST COMMON VALUE FOR 'e' IS '0x10001' or 65537

"""
num = 12 
n = 17 * 23
e = 65537

print(pow(num, e, n)) # This is the "ciphertext"

# Basically encryption is R = msg^e mod n 