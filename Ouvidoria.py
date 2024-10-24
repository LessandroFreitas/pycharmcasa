opcao = -1
manifestacao = []

while opcao != 6:
    print(
        "\n1 » Listagem das Manifestações \n2 » Criar nova Manifestação  \n3 » Exibir quantidade de Manifestações  \n4 » Pesquisar uma manifestação por código \n5 » Excluir uma manifestação pelo código \n6 » sair")
    opcao = int(input("\nDigite uma opção: "))
    print("A opção esolhida foi", opcao)

    if opcao == 1:
        if len(manifestacao) > 0:
            print("Lista de  Manifestações")
            for item in manifestacao:
                print(" » ", item)
        else:
            print("Não existe manifestações!")

    elif opcao == 2:
        novaManifestacao = input("Digite uma nova Manifestacão: ")
        manifestacao.append(novaManifestacao)
        print("Nova Manifestacão criada com sucesso!")

    elif opcao == 3:
        quantidademanifestacao = len(manifestacao)
        print("No momento contem: ", quantidademanifestacao)

    elif opcao == 4:
        posicaoBuscar = int(input("Digite uma posição: "))
        if posicaoBuscar > 0 and posicaoBuscar <= len(manifestacao):
           elemnetoBuscado = manifestacao [posicaoBuscar - 1]
           print("A Manifestação é: ",elemnetoBuscado)
        else:
            print("Posição invalida!")

    elif opcao == 5:
        if len(manifestacao) > 0:
            print("Lista das manifestações")
            for posicao in range (len(manifestacao)):
                print(str(posicao+1)+ "ª posição é ", manifestacao[posicao])

            posicaoRemover = int (input("Digite o número da manifestação a ser removido: "))
            if posicaoRemover > 0 and posicaoRemover <= len(manifestacao):
                manifestacao.pop(posicaoRemover-1)
                print("Manifestacão removida com sucesso!")
            else:
                print("Posição invalida!")
        else:
            print("Não esxistem manifestações para exibir.")

    elif opcao != 6:
        print("Opção inválida")

print("Obrigado por usar nosso software!!!")