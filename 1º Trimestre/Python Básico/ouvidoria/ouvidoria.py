opcao = 0

while True:
    print("Opcão 1: Registrar Manifestação")
    print("Opcão 2: Listar Manifestações")
    print("Opcão 3: Alterar Manifestação")
    print("Opcão 4: Excluir Manifestação")
    print("Opcão 5: Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        def registrar_manifestacao():
            manifestacao = input("Digite a manifestação: ")
            with open("manifestacoes.txt", "a") as arquivo:
                arquivo.write(manifestacao + "\n")
            print("Manifestação registrada com sucesso!")
        registrar_manifestacao()

    elif opcao == 2:
        def listar_manifestacoes():
            with open("manifestacoes.txt", "r") as arquivo:
                manifestacoes = arquivo.readlines()
                print("Manifestações registradas: ")
                for i in range(len(manifestacoes)):
                    print(i + 1, "-", manifestacoes[i])
        listar_manifestacoes()

    elif opcao == 3:
        def alterar_manifestacao():
            listar_manifestacoes()
            manifestacao = int(input("Digite o número da manifestação que deseja alterar: "))
            with open("manifestacoes.txt", "r") as arquivo:
                manifestacoes = arquivo.readlines()
            if 1 <= manifestacao <= len(manifestacoes):
                nova_manifestacao = input("Digite a nova manifestação: ")
                manifestacoes[manifestacao - 1] = nova_manifestacao + "\n"
                with open("manifestacoes.txt", "w") as arquivo:
                    arquivo.writelines(manifestacoes)
                print("Manifestação alterada com sucesso!")
            else:
                print("Número da manifestação inválido.")
        alterar_manifestacao()

    elif opcao == 4:
        def excluir_manifestacao():
            listar_manifestacoes()
            manifestacao = int(input("Digite o número da manifestação que deseja excluir: "))
            with open("manifestacoes.txt", "r") as arquivo:
                manifestacoes = arquivo.readlines()
            if 1 <= manifestacao <= len(manifestacoes):
                manifestacoes.pop(manifestacao - 1)
                with open("manifestacoes.txt", "w") as arquivo:
                    arquivo.writelines(manifestacoes)
                print("Manifestação excluída com sucesso!")
            else:
                print("Número da manifestação inválido.")
        excluir_manifestacao()

    elif opcao == 5:
        print("Sair")
        break
    else:
        print("Opção inválida")