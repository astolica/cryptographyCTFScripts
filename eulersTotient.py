"""
 RSA relies on the difficulty of the modulus N 
 If the prime factors can be found out, you can calculate 
 the Euler totient of N and decrypt the ciphertext!!!

 What is Euler's totient?
 It calculates how many positive integers up to "n" share 
 no common factors other than 1 with n 
 """

p = 857504083339712752489993810777
q = 1029224947942998075080348647219 

n = p * q

#print(totient(n)) do not run this if you don't want your pc to overheat

euler = (p-1) * (q-1) # this is euler's totient! applied here only if p and q are different primes 
print(euler)

