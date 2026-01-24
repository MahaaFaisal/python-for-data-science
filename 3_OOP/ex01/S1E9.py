from abc import ABC, abstractmethod


class Character(ABC):
    """A class that represents a character"""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name if isinstance(first_name, str) else None
        if self.first_name is None:
            print("ValueError: first_name should be a string. Now set to None")

        self.is_alive = is_alive if isinstance(is_alive, bool) else True
        if not isinstance(is_alive, bool):
            print("ValueError: is_alive should be a bool. Now set to True")

    @abstractmethod
    def die(self):
        """ changes the is_alive attribute to false"""
        self.is_alive = False


class Stark(Character):
    """A character from the Starks"""

    def die(self):
        """ calls super.die() which changes the is_alive attribute to false"""
        super().die()
