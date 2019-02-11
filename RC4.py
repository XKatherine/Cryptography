import sys

def KSA(key):
    keylength = len(key)

    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]
        yield K

def convert_key(s):
    return [ord(c) for c in s]


def RC4(key):
    S = KSA(key)
    return PRGA(S)


if __name__ == '__main__':

    key = "54780484"
    plaintext = "AE1BA189DC1F10F4C258BF7B45B220F5"

    key = convert_key(key)
    keystream = RC4(key)


    for c in bytes.fromhex(plaintext):
        print("%02X" % (c ^ keystream.__next__()))
