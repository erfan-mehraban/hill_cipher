import numpy
from numpy import matrix
from numpy import linalg

class ModMatrix(matrix):

    def mod_inverse(self, p):
        """ Finds the inverse of self matrix mod p
        """
        n = len(self)
        A = matrix(self)
        adj = numpy.zeros(shape=(n, n))
        for i in range(0, n):
            for j in range(0, n):
                adj[i][j] = ((-1)**(i + j) *
                            int(round(linalg.det(self.minor(j, i))))) % p
        return (self.det_mod_inv(p) * adj) % p

    def det_mod_inv(self, p):
        """ Finds the inverse of a mod p, if it exists
        """
        a = int(round(linalg.det(self)))
        for i in range(1, p):
            if (i * a) % p == 1:
                return i
        raise ValueError(str(a) + " has no inverse mod " + str(p))

    def minor(self, i, j):
        """ Return matrix A with the ith row and jth column deleted
        """
        A = numpy.array(self)
        minor = numpy.zeros(shape=(len(A) - 1, len(A) - 1))
        p = 0
        for s in range(0, len(minor)):
            if p == i:
                p = p + 1
            q = 0
            for t in range(0, len(minor)):
                if q == j:
                    q = q + 1
                minor[s][t] = A[p][q]
                q = q + 1
            p = p + 1
        return minor

    def is_invertible(self, p):
        matrix_invertible = self.shape[0] == self.shape[1] and numpy.linalg.matrix_rank(self) == self.shape[0]
        try:
            self.det_mod_inv(p)
        except:
            return False
        return matrix_invertible
