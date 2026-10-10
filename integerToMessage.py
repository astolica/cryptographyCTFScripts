from Crypto.Util.number import * 
""" 
Script converts an integer message to bytes, then decodes the bytes"""

integer_message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269 

byte_msg = long_to_bytes(integer_message)

print(byte_msg.decode()) 