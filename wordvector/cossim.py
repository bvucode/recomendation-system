import math
import operator

class CosSim:
    def __init__(self, vect1, vect2):
        self.vect1 = vect1
        self.vect2 = vect2

    def cossim(self):
        # Целиком отсюда: http://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists
        def dot_product2(v1, v2):
            return sum(map(operator.mul, v1, v2))

        def vector_cos5(v1, v2):
            prod = dot_product2(v1, v2)
            len1 = math.sqrt(dot_product2(v1, v1))
            len2 = math.sqrt(dot_product2(v2, v2))
            return prod / (len1 * len2)

        return vector_cos5(self.vect1, self.vect2)
