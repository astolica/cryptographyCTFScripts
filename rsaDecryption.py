N = 882564595536224140639625987659416029426239230804614613279163 # public 
e = 6553765537 # thing to exponentiate by 

cipherText = 77578995801157823671636298847186723593814843845525223303932 # encrypted ciphertext with exponent e and modulus N 
key = 121832886702415731577073962957377780195510499965398469843281 # key from before where we used Euler's totient to calculate 
"""
Remember that the key is the modular multiplicative inverse of the exponent e modulo ϕ(N)"""
m = pow(cipherText, key, N) 
print(m)