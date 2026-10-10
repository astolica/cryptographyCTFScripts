import base64 

h_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
decoded = bytes.fromhex(h_string)
encoded = base64.b64encode(decoded) # encode the base64 stuff 

print(encoded.decode()) # decode() here just removes the b'' label on the string 