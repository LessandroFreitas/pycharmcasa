opcao = 0
manifestacoes = []

while opcao != "6":
    print(
        "\n1 » Listagem das Manifestações"
        "\n2 » Criar nova Manifestação"
        "\n3 » Exibir quantidade de Manifestações"
        "\n4 » Pesquisar uma manifestação por código"
        "\n5 » Excluir uma manifestação pelo código"
        "\n6 » Sair")
    opcao = input("\nDigite uma opção: ")

    if opcao == "1":
        if len(manifestacoes) > 0:
            print("Essas são as manifestações cadastradas no nosso sistema: ")
            for i in range(len(manifestacoes)):
                print(str(i + 1), "-", manifestacoes[i])
        else:
            print("Não existem manifestações cadastradas.")

    elif opcao == "2":
        novaManifestacao = input("Digite a sua manifestação: ")
        manifestacoes.append(novaManifestacao)
        print("Manifestação cadastrada com sucesso!")

    elif opcao == "3":
        quantidadeDeManifestacoes = len(manifestacoes)
        if quantidadeDeManifestacoes != 0:
            print('Existem', quantidadeDeManifestacoes, 'manisfestações cadastradas!')
        else:
            print("Não existem manifestações cadastradas")

    elif opcao == "4":
        if len(manifestacoes) > 0:
            posicaoBuscar = int(input("Digite o código da manifestação que você deseja buscar: "))
            if posicaoBuscar > 0 and posicaoBuscar <= len(manifestacoes):
                elementoBuscado = manifestacoes[posicaoBuscar - 1]
                print("A Manifestação é:", elementoBuscado)
            else:
                print("Manifestação inexistente!")
        else:
            print("Não existem manifestações cadastradas.")

    elif opcao == "5":
        if len(manifestacoes) > 0:
            codigoDaManifestacao = int(input("Digite o código da manifestação que você deseja excluir: "))
            if codigoDaManifestacao > 0 and codigoDaManifestacao <= len(manifestacoes):
                manifestacoes.pop(codigoDaManifestacao - 1)
                print('Manifestação excluída com sucesso!')
            else:
                print('Manifestação não encontrada!')
        else:
            print("Não existem manifestações cadastradas.")

    elif opcao != "6":
        print("Opção inválida")

print("Obrigado por usar nosso sistema!!!")