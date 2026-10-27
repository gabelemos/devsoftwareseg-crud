from manager import GestaoEscola

def main():
    gestao = GestaoEscola()
    
    print("--- Bem-vindo ao Sistema de Gestão de Academia ---")
    print("Logado como: Administrador")
    
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Listar Alunos")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            name = input("Nome do aluno: ")
            plan = input("Plano: ")
            gestao.add_student(name, plan)
            print("Aluno cadastrado com sucesso!")
            
        elif choice == '2':
            name = input("Nome do professor: ")
            specialty = input("Especialidade: ")
            gestao.add_professor(name, specialty)
            print("Professor cadastrado com sucesso!")

        elif choice == '3':
            print("\nLista de Alunos:")
            for s in gestao.estudantes:
                print(f"ID: {s.id} | Nome: {s.name} | Plano: {s.plan}")
        
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
