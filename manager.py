from models import Estudante, Professor, Plano, Treinamento

class GestaoEscola:
    def __init__(self):
        self.estudantes = []
        self.professores = []
        self.planos = []
        self.treinamentos = []
        self._id_counter = 1

    def add_student(self, name, plan):
        estudante = Estudante(self._id_counter, name, plan)
        self.estudantes.append(estudante)
        self._id_counter += 1
        return estudante

    def add_professor(self, name, specialty):
        professor = Professor(self._id_counter, name, specialty)
        self.professores.append(professor)
        self._id_counter += 1
        return professor
