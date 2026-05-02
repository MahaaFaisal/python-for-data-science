import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random lowercase identifier with fifteen characters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_username(name: str, surname: str) -> str:
    """Return a login username from the first name initial and surname."""
    return name[0] + surname


@dataclass
class Student:
    """Represent a student with generated login and id fields."""

    name: string
    surname: string
    active: bool = True
    login: string = field(init=False)
    id: string = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Initialize the login field after dataclass construction."""
        self.login = self.name[0] + self.surname
