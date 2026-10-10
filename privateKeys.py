"""
The private key is the secret piece of information, 
or "trapdoor", which allows us to quickly invert the encryption function.

if you do not have the private key the fastest way to decrypt the 
ciphertext is to factorise the modulus which is very hard to do for large integers
"""

p = 857504083339712752489993810777
q = 1029224947942998075080348647219 

n = p*q
euler = (p-1) * (q-1)
e = 65537
"""THIS LINE BELOW is the modular multiplicative inverse of the exponent e 
modulo ϕ(N)
Essentially, the private key!
"""
d = pow(e, -1, euler) 

print(d)