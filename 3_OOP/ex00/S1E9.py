from abc import ABC, abstractmethod


class Character(ABC):
    """A class that represents a character"""
    def __init__(self, first_name, is_alive=True):
        """ initializes the character with name and optional is_alive"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """ changes the is_alive attribute to false"""
        self.is_alive = False


class Stark(Character):
    """A character from the Starks"""
    def die(self):
        """ calls super.die() which changes the is_alive attribute to false"""
        super().die()


Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

# hodor = Character("hodor") # cause an error
