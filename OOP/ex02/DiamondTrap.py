from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ A class that inherits from Baratheon and Lannister"""
    def __init__(self, first_name):
        """ the initialization function for Lannister"""
        super().__init__(first_name)

    def set_eyes(self, eyes: str) -> None:
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        self.hairs = hairs

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs





Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
