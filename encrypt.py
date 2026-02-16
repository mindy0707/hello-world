plaintext = input("Enter the plaintext: ")
distance = int(input("Enter the distance value: "))

encrypted = ""

for ch in plaintext:
    # get the ASCII code
    code = ord(ch)

    # shift it
    code = code + distance

    # wrap around printable ASCII (32–126)
    if code > 126:
        code = 32 + (code - 127)
    elif code < 32:
        code = 127 - (32 - code)

    encrypted += chr(code)

print("Encrypted text:", encrypted)
