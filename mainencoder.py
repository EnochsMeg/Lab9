## megan enochs encoder code

def encode(string):
    password = ''
    encode1 = 0
    for num in string:
        encode1 = int(num)+3
        password += string(encode1)
        encode1 = 0
    return password