
def Encryption(msg):
    lstOut = []
    for s in msg:
        asciiNum = ord(s) + 3
        lstOut.append(chr(asciiNum))

    return "".join(lstOut)

