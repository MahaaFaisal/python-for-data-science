import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_username(name: str, surname: str) -> str:
    return name[0] + surname


@dataclass
class Student:
    name: string
    surname: string
    active: bool = True
    login: string = field(init=False)
    id: string = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname


student = Student(name="Edward", surname="agle")
print(student)
