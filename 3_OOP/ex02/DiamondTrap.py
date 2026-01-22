from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ A class that inherits from Baratheon and Lannister"""
    def __init__(self, first_name, is_alive=True):
        """ the initialization function for Lannister"""
        super().__init__(first_name, is_alive)

    @property
    def _eyes(self) -> str:
        return self.__dict__["eyes"]

    @property
    def _hairs(self) -> str:
        return self.__dict__["hairs"]

    @_eyes.setter
    def _eyes(self, value: str) -> None:
        self.__dict__["eyes"] = value

    @_hairs.setter
    def _hairs(self, value: str) -> None:
        self.__dict__["hairs"] = value

    def set_eyes(self, value: str) -> None:
        print("eyes setter")
        self.eyes = value

    def set_hairs(self, value: str) -> None:
        self.hairs = value

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs


# Joffrey = King("Joffrey")
# print(Joffrey.__dict__)
# Joffrey.set_eyes("blue")
# Joffrey.set_hairs("light")
# print(Joffrey.get_eyes())
# print(Joffrey.get_hairs())
# print(Joffrey.__dict__)
print(King.__mro__)
