""" 
Trapdoor function!
Easy to compute in one direction, but difficult to compute in the other!
Widely used in public key cryptography 
The key, of course, is what makes reversing a function trivial
Modular exponentiation, along with prime factorization, allows us to build this trapdoor function
"""
print(pow(101, 17, 22663)) # example of calculating a modular exponentiation problem
# arguments for the pow() function are pow(base, exponent, modulus)
