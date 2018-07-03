import numpy
from matrix import ModMatrix
from message import Message
class BaseHillCipher:
    alphabet_size = 26
    key_size = 2

    def __init__(self, alphabet_size=26, key_size=2, key=None):
        self.alphabet_size = alphabet_size
        self.key_size = key_size
        if key is not None:
            self.set_key(key)
        else:
            self.set_key(self._generate_key(key_size))

    def set_key(self, key):
        self._key = key

    def _generate_key(self, size):
        temp = ModMatrix(numpy.random.randint(self.alphabet_size, size=(size, size)))
        if not temp.is_invertible(self.alphabet_size):
            return self._generate_key(size)
        print ("*****",temp.is_invertible)
        return temp
    
    def inverse_key(self):
        self._key = self._key.mod_inverse(self.alphabet_size)

class HillCipherEncrypter(BaseHillCipher):

    def encrypt(self, msg):
        coded_msg = Message(msg, self.key_size)
        encrypted_matrix = self._key * coded_msg % self.alphabet_size
        encrypted_msg = Message._decode(encrypted_matrix)
        print("coded message:\n", coded_msg)
        print("key:\n", self._key)
        print("encrypted message matrix:\n", encrypted_matrix)
        print("encrypted message:\n", encrypted_msg)
        return encrypted_msg

class HillCipherDecrypter(BaseHillCipher):

    def decrypt(self, msg):
        coded_msg = Message(msg, self.key_size)
        self.inverse_key()
        decrypted_matrix = self._key * coded_msg % self.alphabet_size
        decrypted_msg = Message._decode(decrypted_matrix)
        print("coded message:\n", coded_msg)
        print("inverse key:\n", self._key)
        print("decrypted message matrix:\n", decrypted_matrix)
        print("decrypted message:\n", decrypted_msg)
        return decrypted_msg