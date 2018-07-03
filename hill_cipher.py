import numpy
from matrix import ModMatrix
from message import Message
class BaseHillCipher:
    """ Hill Cipher Base classes
    every hill cipher classes should inherit from this class
    this class support key functions: generating, setting and inverting
    """
    alphabet_size = 26
    key_size = 2

    def __init__(self, alphabet_size=26, key_size=2, key=None):
        """ initialize base hill cipher datas
        defualt alphabat size is english alhphabet lenght
            (for changing it make sure code_table in messege class supports it)
        if no key provide, class will generate it randomly
        """
        self.alphabet_size = alphabet_size
        self.key_size = key_size
        if key is not None:
            self.set_key(key)
        else:
            self.set_key(self._generate_key(key_size))

    def set_key(self, key):
        self._key = key

    def _generate_key(self, size):
        """ generating randomly valid key
        the key should be n*n there n = self.alphabet_size
        also it should be invertible
        """
        temp = ModMatrix(numpy.random.randint(self.alphabet_size, size=(size, size)))
        if not temp.is_invertible(self.alphabet_size):
            return self._generate_key(size)
        return temp
    
    def inverse_key(self):
        """ inversing key and set it as self._key
        """
        self._key = self._key.mod_inverse(self.alphabet_size)

class HillCipherEncrypter(BaseHillCipher):
    """ encrypting message
    this class implemented encrypt function wich encrypt message with key wich saved in class"""

    def encrypt(self, msg):
        # first code message and creating matrix from it
        coded_msg = Message(msg, self.key_size)
        # multiply key with coded message to create encrypted matrix message
        encrypted_matrix = self._key * coded_msg % self.alphabet_size
        # decode encrypted message to human readble charecters
        encrypted_msg = Message._decode(encrypted_matrix)
        print("coded message:\n", coded_msg)
        print("key:\n", self._key)
        print("encrypted message matrix:\n", encrypted_matrix)
        print("encrypted message:\n", encrypted_msg)
        return encrypted_msg

class HillCipherDecrypter(BaseHillCipher):
    """ decrypting message
    this class implemented decrypt function wich decrypt message with key wich saved in class"""

    def decrypt(self, msg):
        # first code message and creating matrix from it
        coded_msg = Message(msg, self.key_size)
        # creating inverse key for decoding proccess
        self.inverse_key()
        # multiply inversed key with coded message to create decrypted matrix message
        decrypted_matrix = self._key * coded_msg % self.alphabet_size
        # decode decrypted message to human readble format
        decrypted_msg = Message._decode(decrypted_matrix)
        print("coded message:\n", coded_msg)
        print("inverse key:\n", self._key)
        print("decrypted message matrix:\n", decrypted_matrix)
        print("decrypted message:\n", decrypted_msg)
        return decrypted_msg
