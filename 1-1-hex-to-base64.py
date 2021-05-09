import binascii

input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# Convert the hex to bytes
bytes = binascii.a2b_hex(input)
print(bytes)
# => b"I'm killing your brain like a poisonous mushroom"

# Pass the bytes to base64
base64 = binascii.b2a_base64(bytes, newline=False)
print(base64)
# => b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n'

# Convert to a string and and strip whitespace to match expected output
cleaned_result = base64.decode()
print(cleaned_result)
# => SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

print(cleaned_result == expected)
# => True
