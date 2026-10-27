from dataclasses import dataclass
from typing import List

@dataclass
class Plano:
    id: int
    name: str
    price: float

@dataclass
class Estudante:
    id: int
    name: str
    plan: str

@dataclass
class Professor:
    id: int
    name: str
    specialty: str

@dataclass
class Treinamento:
    id: int
    student_name: str
    details: str
