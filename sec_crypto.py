from crypto import *

class SecCrypto():
    def load_table(self, cache):
        for a in range(len(T)):
            cache.write_address(T_address+a, T[a])
    
    def feistel_encrypt(self, cache, msg, key):
        l0 = ord(msg[0])
        r0 = ord(msg[1])
        r1 = cache.read_address(r0)
        r1 = l0 ^ ord(key[0]) ^r1[0]
        l1 = r0
        r2 = cache.read_address(r1)
        r2 = l1 ^ ord(key[1]) ^r2[0]
        l2 = l1
        self.load_table(cache)
        return chr(l2)+chr(r2)
