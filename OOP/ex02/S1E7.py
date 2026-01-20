from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """ the initialization function for Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):
        """ the reprsentation function for Baratheon"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __str__(self):
        """ the str function for Baratheon"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def die(self):
        """ A function that calls super.die() which sets is_alive to false"""
        super().die()

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        """ a function that creates a new Baratheon object \
        and returns the cls object for chaining"""
        return cls(first_name, is_alive)


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """ the initialization function for Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        """ the reprsentation function for Lannister"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __str__(self):
        """ the str function for Lannister"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def die(self):
        """ A function that calls super.die() which sets is_alive to true"""
        super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """ a function that creates a new Lannister object \
            and returns the cls object for chaining"""
        return cls(first_name, is_alive)
