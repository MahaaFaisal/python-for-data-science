

class calculator:
    """a class that allows, multiplication, addition, substration\
        and division of a vector by a scaler"""

    def __init__(self, vector: list):
        """initialization of calculator"""
        if isinstance(vector, list) and all(
             isinstance(x, (int, float)) for x in vector):
            self._vector = vector
        else:
            print("ValueError: object should be a list of ints and floats.\
                  initialized to []")
            self._vector = []

    def __add__(self, object) -> None:
        """adds a scaler to vector element"""
        if (isinstance(object, (int, float))):
            self._vector = [x + object for x in self._vector]
            print(self._vector)
        else:
            print("ValueError: scaler should be int or float.Vector unchanged")

    def __mul__(self, object) -> None:
        """multiplies vector elements by a scaler"""
        if (isinstance(object, (int, float))):
            self._vector = [x * object for x in self._vector]
            print(self._vector)
        else:
            print("ValueError: scaler should be int or float.Vector unchanged")

    def __sub__(self, object) -> None:
        """subatracts a scaler from vector elements"""
        if (isinstance(object, (int, float))):
            self._vector = [x - object for x in self._vector]
            print(self._vector)
        else:
            print("ValueError: scaler should be int or float.Vector unchanged")

    def __truediv__(self, object) -> None:
        """divides vector elements by a scaler"""
        try:
            if (isinstance(object, (int, float))):
                self._vector = [x / object for x in self._vector]
                print(self._vector)
            else:
                print("ValueError: scaler should be int or float.\
                      Vector unchanged")

        except ZeroDivisionError as e:
            print(f"{type(e).__name__}: {e}")


v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])

print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
