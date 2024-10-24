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
elif opcao == 4:
    print("Pesquisar uma manifestação por código")
elif opcao == 5:
    print("Excluir uma manifestação pelo código")
elif opcao != 6:
    print("Opção inválida")

print("Obrigado por usar nosso software!!!")
