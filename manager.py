from models import Estudante, Professor, Plano, Treinamento

class GestaoEscola:
    def __init__(self):
        self.estudantes = []
        self.professores = []
        self.planos = []
        self.treinamentos = []
        self._id_counter_student = 1
        self._id_counter_professor = 1
        self._id_training = 1

    def add_student(self, name, plan, professor_id): 
        estudante = Estudante(self._id_counter_student, name, plan, professor_id)
        self.estudantes.append(estudante)
        self._id_counter_student += 1
        return estudante

    def add_professor(self, name, specialty): 
        professor = Professor(self._id_counter_professor, name, specialty)
        self.professores.append(professor)
        self._id_counter_professor += 1
        return professor

    def add_training (self, student_id, details): #JR: Adicionei funcao de treinamento pro professor escrever o treino do aluno
        treinamento = Treinamento(self._id_training, student_id, details) 
        self.treinamentos.append(treinamento)
        self._id_training += 1

    def delete_student(self, student_id):
        for estudante in self.estudantes:
            if estudante.id == student_id:
                self.estudantes.remove(estudante)
                return True
        return False


    def delete_professor(self, professor_id):
        for professor in self.professores:
            if professor.id == professor_id:
                self.professores.remove(professor)
                return True
        return False
