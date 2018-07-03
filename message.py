import numpy
import math
from matrix import ModMatrix

class Message(ModMatrix):
    """ coding and decoding message with code_table
    """

    # code dictionary wich gives you int for givven letter. it is generating automatically
    code_table = {chr(i):i-97 for i in range(97,123)}

    def __new__(cls, msg, height, *args, **kwargs):
        """ coding message and add it to matrix
        """
        if  "dtype" in kwargs: # make sure it is integer format
            del kwargs["dtype"]
        return super().__new__(cls, cls._code(msg, height), *args, dtype = numpy.int32, **kwargs)

    def decode(self):
        return self._decode(self)

    @staticmethod
    def _code(msg, height):
        """ coding string to matrix with height given
        """
        # for supporting captal letters
        msg = msg.lower()
        # calculating width of coded matrix
        width = math.ceil(len(msg)/height)
        # default value is 0 (so no white space allowed)
        coded_data = numpy.zeros(shape=(height, width))
        # fill coded matrix line by line
        for row in range(height):
            for culmn in range(width):
                string_index = culmn+row*width
                if string_index < len(msg):
                    coded_data[row][culmn] = Message.code_table[msg[string_index]]
        return coded_data
    
    @staticmethod
    def _decode(coded_matrix):
        """ decoding matrix to string
        """
        coded_matrix = coded_matrix.A
        decode_string = ""
        for row in coded_matrix:
            for cell in row:
                decode_string += chr(int(cell+97))
        return decode_string
