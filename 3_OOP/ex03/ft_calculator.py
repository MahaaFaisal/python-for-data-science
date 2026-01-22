

class calculator:
    """a class that allows, multiplication, addition, substration\
        and division of a vector by a scaler"""

    def __init__(self, object: list):
        """initialization of calculator"""
        self._list = object

    def __add__(self, object) -> None:
        """adds a scaler to vector element"""
        self._list = [x + object for x in self._list]
        print(self._list)

    def __mul__(self, object) -> None:
        """multiplies vector elements by a scaler"""
        self._list = [x * object for x in self._list]
        print(self._list)

    def __sub__(self, object) -> None:
        """subatracts a scaler from vector elements"""
        self._list = [x - object for x in self._list]
        print(self._list)

    def __truediv__(self, object) -> None:
        """divides vector elements by a scaler"""
        try:
            self._list = [x / object for x in self._list]
            print(self._list)
        except ZeroDivisionError as e:
            print(f"{type(e).__name__}: {e}")


v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
