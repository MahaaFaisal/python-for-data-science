from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ A class that inherits from Baratheon and Lannister"""

    def __init__(self, first_name, is_alive=True):
        """ the initialization function for King"""
        super().__init__(first_name, is_alive)

    @property
    def eyes(self) -> str:
        """eyes property for King"""
        return self.__dict__["eyes"]

    @property
    def hairs(self) -> str:
        """hairs property for King"""
        return self.__dict__["hairs"]

    @eyes.setter
    def eyes(self, value: str) -> None:
        """eyes property setter for King"""
        if isinstance(value, str):
            self.__dict__["eyes"] = value
        else:
            print("ValueError: eyes value should be a string")

    @hairs.setter
    def hairs(self, value: str) -> None:
        """hairs property setter for King"""
        if isinstance(value, str):
            self.__dict__["hairs"] = value
        else:
            print("ValueError: hairs value should be a string")

    def set_eyes(self, value: str) -> None:
        """uses property setter to change eyes"""
        self.eyes = value

    def set_hairs(self, value: str) -> None:
        """uses property setter to change hairs"""
        self.hairs = value

    def get_eyes(self) -> str:
        """uses property to return eyes"""
        return self.eyes

    def get_hairs(self) -> str:
        """uses property to return hairs"""
        return self.hairs


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
