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
    professor_id: int #JR: Adicionei um professor_id (pra saber com qual professor o aluno da aula)

@dataclass
class Professor:
    id: int
    name: str
    specialty: str

@dataclass
class Treinamento:
    id: int
    student_id: int
    details: str
