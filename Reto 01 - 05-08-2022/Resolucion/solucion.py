class Reto:

    def solve(self, vector):
        """ Implementación del reto mediante copias de vectores """

        if len(vector) <= 2:
            return False
        else:
            for i in range(len(vector)):
                vectorCopy = vector.copy()
                vectorCopy.pop(i)
                if self.__isStrictlyDecreasing(vectorCopy):
                    return True
            return False

    def __isStrictlyDecreasing(self, vector):
        """ Devuelve true si vector es estrictamente decreciente. False en caso contrario """

        for i in range(0, len(vector) - 1, 1):
            if (vector[i] >= vector[i + 1]):
                return False
        return True

    def solveNoCopy(self, vector):
        """ Implementación del reto sin copia de vectores """

        if len(vector) <= 2:
            return False
        else:
            for i in range(len(vector)):
                if self.__isStrictlyDecreasingNoCopy(vector, i):
                    return True
            return False

    def __isStrictlyDecreasingNoCopy(self, vector, i):
        """ Devuelve true si al eliminar el elemento i-esimo de vector, este es estrictamente decreciente. False en caso contrario """

        indexes = [i for i in range(len(vector))]
        indexes.pop(i)
        for i in range(0, len(indexes) - 1, 1):
            if (vector[indexes[i]] >= vector[indexes[i + 1]]):
                return False
        return True

v0 = [1, 2, 3]
v1 = [1]
v2 = [1, 2]
v3 = [1, 1]
v4 = [2, 1]
v5 = [1,2,10,5,7]
v6 = [1, 2, 3, 4]
v7 = [1, 2, 3, 2]
v8 = []
v9 = [2, 3, 1, 2]
v10 = [1, 1, 1, 1, 1]
v11 = [1, 7, 8, 4, 8]

vectors = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]
reto = Reto()

for v in vectors:
    print(v, reto.solve(v), reto.solveNoCopy(v))
