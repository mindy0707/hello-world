encrypted = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))

plaintext = ""

for ch in encrypted:
    # get ASCII code
    code = ord(ch)

    # shift backward
    code = code - distance

    # wrap around printable ASCII (32–126)
    if code < 32:
        code = 127 - (32 - code)
    elif code > 126:
        code = 32 + (code - 127)

    plaintext += chr(code)

print("Plaintext:", plaintext)
