opcao = 6

filmes = []
filmes_alugados = []

while opcao != 5:
    print("Opcão 1: Cadastrar Filme")
    print("Opcão 2: Listar Filmes")
    print("Opcão 3: Alugar Filme")
    print("Opcão 4: Devolver Filme")
    print("Opcão 5: Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Qual filme deseja cadastrar?")
        def cadastrar_filme():
            nome = input("Digite o nome do filme: ")
            filmes.append(nome)
            print("Filme cadastrado com sucesso!")
        cadastrar_filme()

    elif opcao == 2:
        print("Filmes cadastrados: ")
        def filmes_cadastrados(lista):
            for i in range(len(lista)):
                print(i + 1, "-", lista[i])
        filmes_cadastrados(filmes)

    elif opcao == 3:
        print("Alugar Filme")
        if not filmes:
            print("Nenhum filme disponível para alugar.")
        else:
            filmes_cadastrados(filmes)
            filme = int(input("Digite o número do filme que deseja alugar: "))
            if 1 <= filme <= len(filmes):
                filmes_alugados.append(filmes[filme - 1])
                filmes.pop(filme - 1)
                print("Filme alugado com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == 4:
        print("Qual filme deseja devolver?")
        if not filmes_alugados:
            print("Nenhum filme para devolver.")
        else:
            filmes_cadastrados(filmes_alugados)
            filme = int(input("Digite o número do filme que deseja devolver: "))
            if 1 <= filme <= len(filmes_alugados):
                filmes.append(filmes_alugados[filme - 1])
                filmes_alugados.pop(filme - 1)
                print("Filme devolvido com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == 5:
        print("Sair")

    else:
        print("Opção inválida")
