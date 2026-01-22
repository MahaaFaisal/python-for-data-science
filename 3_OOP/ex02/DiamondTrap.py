from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ A class that inherits from Baratheon and Lannister"""
    def __init__(self, first_name, is_alive=True):
        """ the initialization function for Lannister"""
        super().__init__(first_name, is_alive)

    @property
    def _eyes(self) -> str:
        """eyes property for King"""
        return self.__dict__["eyes"]

    @property
    def _hairs(self) -> str:
        """hairs property for King"""
        return self.__dict__["hairs"]

    @_eyes.setter
    def _eyes(self, value: str) -> None:
        """eyes property setter for King"""
        self.__dict__["eyes"] = value

    @_hairs.setter
    def _hairs(self, value: str) -> None:
        """hairs property setter for King"""
        self.__dict__["hairs"] = value

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
