import base64

string_to_decode = str(input("Give a base64 string: "))

print(base64.b64decode(string_to_decode).decode())