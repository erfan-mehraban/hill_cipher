import numpy
import math
from matrix import ModMatrix

class Message(ModMatrix):
    code_table = {chr(i):i-97 for i in range(97,123)}

    def __new__(cls, msg, height, *args, **kwargs):
        if  "dtype" in kwargs:
            del kwargs["dtype"]
        return super().__new__(cls, cls._code(msg, height), *args, dtype = numpy.int32, **kwargs)

    def decode(self):
        return self._decode(self)

    @staticmethod
    def _code(msg, height):
        width = math.ceil(len(msg)/height)
        coded_data = numpy.zeros(shape=(height, width))
        for row in range(height):
            for culmn in range(width):
                string_index = culmn+row*width
                if string_index < len(msg):
                    coded_data[row][culmn] = Message.code_table[msg[string_index]]
        return coded_data
    
    @staticmethod
    def _decode(coded_matrix):
        coded_matrix = coded_matrix.A
        decode_string = ""
        for row in coded_matrix:
            for cell in row:
                decode_string += chr(int(cell+97))
        return decode_string
