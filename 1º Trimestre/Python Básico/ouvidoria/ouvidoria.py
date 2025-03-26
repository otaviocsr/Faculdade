opcao = 0
manifestacoes = []

while True:
    print("=" * 35)
    print("Opcão 1: Registrar Manifestação")
    print("Opcão 2: Listar Manifestações")
    print("Opcão 3: Excluir Manifestação")
    print("Opcão 4: Sair")
    print("=" * 35)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        def registrar_manifestacao():
            manifestacao = input("Digite a manifestação: ")
            manifestacoes.append(manifestacao)
            print("Manifestação registrada com sucesso!")
        registrar_manifestacao()

    elif opcao == 2:
        def listar_manifestacoes():
            print("Manifestações registradas: ")
            for i, manifestacao in enumerate(manifestacoes, start=1):
                print(i, "-", manifestacao)
        listar_manifestacoes()

    elif opcao == 3:
        def excluir_manifestacao():
            listar_manifestacoes()
            manifestacao = int(input("Digite o número da manifestação que deseja excluir: "))
            if 1 <= manifestacao <= len(manifestacoes):
                manifestacoes.pop(manifestacao - 1)
                print("Manifestação excluída com sucesso!")
            else:
                print("Número da manifestação inválido.")
        excluir_manifestacao()

    elif opcao == 4:
        print("Sair")
        break
    else:
        print("Opção inválida")
