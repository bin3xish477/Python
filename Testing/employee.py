from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Employee(object):
    raise_amt: ClassVar[float] = 1.05
    first_name:str
    last_name:str
    salary:float

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)