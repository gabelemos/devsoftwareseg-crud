from manager import GestaoEscola

def main():
    gestao = GestaoEscola()
    while True: 
        print("--- Bem-vindo ao Sistema de Gestão de Academia ---")
        print("\nMenu de Login:")
        print("1. Entrar como Administrador")
        print("2. Entrar como Professor")
        print("3. Entrar como Aluno")
        print("4. Encerrar Programa")

        opcao_geral = str(input("Escolha a opção de login: "))

        if opcao_geral == "1": #JR: Login Administrador
            while True:
                print("\nMenu do Administrador:")
                print("1. Cadastrar Aluno")
                print("2. Cadastrar Professor")
                print("3. Listar Alunos")
                print("4. Listar Professor")
                print("5. Deletar Aluno")
                print("6. Deletar Professor")
                print("7. Voltar")

                opcao_adm = input("Escolha uma opção: ")

                if opcao_adm == '1':
                    name = input("Nome do aluno: ")
                    plan = input("Plano [Mensal] ou [Anual]: ")
                    professor_id = int(input("Id do Professor responsável: "))
                    gestao.add_student(name, plan, professor_id)
                    print("Aluno cadastrado com sucesso!")

                elif opcao_adm == '2':
                    name = input("Nome do professor: ")
                    specialty = input("Especialidade: ")
                    gestao.add_professor(name, specialty)
                    print("Professor cadastrado com sucesso!")

                elif opcao_adm == '3':
                    print("\nLista de Alunos:")
                    for s in gestao.estudantes:
                        print(f"ID: {s.id} | Nome: {s.name} | Plano: {s.plan} | Professor: {s.professor_id}")

                elif opcao_adm == '4':
                    print("\nLista de Professores:")
                    for s in gestao.professores:
                        print(f"ID: {s.id} | Nome: {s.name} | Plano: {s.specialty}")

                elif opcao_adm == '5':
                    estudante_id = int(input("Digite o ID do aluno que você deseja excluir: "))
                    if gestao.delete_student(estudante_id):
                        print("Aluno excluído com sucesso")
                    else:
                        print("Aluno não encontrado")

                elif opcao_adm == '6':
                    professor_id = int(input("Digite o ID do professor que você deseja excluir: "))
                    if gestao.delete_professor(professor_id):
                        print("Professor excluído com sucesso")
                    else:
                        print("Professor Não encontrado")

                elif opcao_adm == '7':
                    print("Deslogando")
                    break

        elif opcao_geral == "2": #JR: Login do Professor

            professor_id = int(input("Digite seu ID de Professor: ")) #JR: Testando qual professor é, pra saber quais alunos ele é responsavel

            professor_logado = None

            for professor in gestao.professores:
                if professor.id == professor_id:
                    professor_logado = professor
                    break

            if professor_logado is None:
                print("Professor não encontrado.")
                continue
            else:
                print(f"\nBem-vindo, Professor {professor_logado.name}!")

            while True: 
                print("\n Menu do Professor:")
                print("1. Listar Alunos")
                print("2. Cadastrar Treinos ")
                print("3. Listar Treinos")
                print("4. Sair")

                opcao_professor = str(input("Escolha uma opção: "))

                if opcao_professor == "1": 

                    print("\nLista de seus Alunos:")
                    encontrou_aluno = False

                    for aluno in gestao.estudantes:
                        if aluno.professor_id == professor_logado.id:
                            print(f"ID: {aluno.id} | "
                                  f"Nome: {aluno.name} | "
                                  f"Plano: {aluno.plan}"
                            )
                        encontrou_aluno = True

                    if not encontrou_aluno:
                        print("Você não possui alunos cadastrados.")

                elif opcao_professor == "2":

                    print("\n--- Cadastrar Treino ---")

                    alunos_do_professor = [] #JR: aqui serve pra guardar apenas os alunos do professor logado

                    for aluno in gestao.estudantes:  #JR: Verifica se o id do aluno bate com  o do professor logado
                        if aluno.professor_id == professor_logado.id:
                            alunos_do_professor.append(aluno)

                    if len(alunos_do_professor) == 0:
                        print("Você não possui alunos cadastrados")

                    else:
                        print("\nSeus alunos: ") #JR: Aqui vai mostrar os alunos do professor

                    for aluno in alunos_do_professor:
                        print(f"ID: {aluno.id} | "
                              f"Nome: {aluno.name} | " 
                              f"Plano: {aluno.plan}"
                        )
                    aluno_id = int(input("\nDigite o ID do aluno: "))

                    aluno_encontrado = None

                    for aluno in alunos_do_professor: #JR: Verifica se o ID do aluno corresponde a algum de seus alunos
                        if aluno.id == aluno_id:
                            aluno_encontrado = aluno
                            break
                    if aluno_encontrado is None:
                        print("Aluno não encontrado ou não pertence a você")

                    else: #JR: Aqui voce coloca o treino do aluno
                        details = input("Digite os detalhes do treino: ")

                        gestao.add_training(aluno_id, details)

                        print("Treino cadastrado com sucesso")

                elif opcao_professor == "3":
                    print("\n--- Lista de Treinos ---")

                    encontrou_treino = False

                    for treino in gestao.treinamentos:  #JR: Aqui verifica se o treino pertence ao aluno e se esse aluno pertence ao professor logado
                        for aluno in gestao.estudantes:
                            if treino.student_id == aluno.id and aluno.professor_id == professor_logado.id:
                                print(f"\nID do Treino: {treino.id}"
                                f"\nAluno: {aluno.name}"
                                f"\nDetalhes: {treino.details}"
                                )
                                encontrou_treino = True

                    if not encontrou_treino:
                        print("Nenhum treino cadastrado para seus alunos")

                elif opcao_professor == "4":
                    break

                else:
                    print("Opção inválida")

        elif opcao_geral == "3": #JR: Login do Aluno

            aluno_id = int(input("Digite seu ID de Aluno: ")) #JR: Verifica se o ID digitado é o ID de algum Aluno
            aluno_logado = None

            for aluno in gestao.estudantes:
                if aluno.id == aluno_id:
                    aluno_logado = aluno
                    break

            if aluno_logado is None:
                print("Aluno não encontrado")
                continue
            print(f"\nBem-vindo, {aluno_logado.name}!")

            while True: #JR: Menu Aluno
                print("\n--- Menu do Aluno ---")
                print("1. Ver minhas informações")
                print("2. Ver meus treinos")
                print("3. Sair")

                opcao_aluno = str(input("Escolha uma opção: "))

                if opcao_aluno == "1":
                    print("\n--- Minhas Informações ---") #JR:Mostrar informações do aluno
                    print(f"ID: {aluno_logado.id}")
                    print(f"Nome: {aluno_logado.name}")
                    print(f"Plano: {aluno_logado.plan}")
                    print(f"Professor ID: {aluno_logado.professor_id}")

                elif opcao_aluno == "2": #JR: Mostrar treino do aluno
                    print("\n--- Meus Treinos ---")

                    encontrou_treino = False

                    for treino in gestao.treinamentos:
                        if treino.student_id == aluno_logado.id: #JR: Verifica se o treino pertence ao aluno logado
                            print(f"\nID do Treino: {treino.id}") #JR: Mostra o treino
                            print(f"Detalhes: {treino.details}")

                            encontrou_treino = True

                    if not encontrou_treino:
                        print("Você ainda não possui treinos cadastrados")

                elif opcao_aluno == "3":
                    print("Deslogando")
                    break

                else:
                    print("Opção inválida")
        
        elif opcao_geral == "4":
            print("Programa encerrado")
            break

        else:
            print("Opção inválida")
        


if __name__ == "__main__":
    main()