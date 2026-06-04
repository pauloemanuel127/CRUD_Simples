import functions as f

# Definindo o lista como vazia e começando as funções

lista = f.load_list()

while True:

    print(
        "Bem vindo ao sistema de organização de itens, escolha qual operação você deseja realizar:\n" \
        "1. Adicionar novo item\n" \
        "2. Verificar estoque\n" \
        "3. Atualizar estoque\n" \
        "4. Remover item\n" \
        "5. Sair"
    )

    entrada = input()

    if entrada == "5":
        print("Obrigado por usar nosso sistema!")
        f.save_list(lista)
        break

    elif entrada == "1":

        print(
            "\n[Adicionar item]"
        ) 

        item = str(input("Digite o item a ser inserido no estoque: ")).lower()
        quantidade = int(input("Digite a quantidade desse item: "))

        lista = f.append(lista, item, quantidade)
        f.save_list(lista)
    
    elif entrada == "2":

        print(
            "\n[Verificação de Estoque]"
        )

        item = str(input("Digite o item a ser verificado: ")).lower()

        f.read(lista, item)

    elif entrada == "3":
            
        print(
            "\n[Atualização de Estoque]"
        )
        item = str(input("Digite o item a ser alterado: ")).lower()
        novo_item = str(input("Novo nome (ou aperte Enter para manter o mesmo): ")).lower()
        nova_quantidade = input("Nova quantidade (ou digite -1 para manter a mesma): ")

        while not f.validar(nova_quantidade):
            nova_quantidade = input("Digite uma quantidade válida (ou -1): ")

        lista = f.update(lista, item, novo_item, int(nova_quantidade))
        f.save_list(lista)
    
    elif entrada == "4":

        print(
            "\n[Remover item]"
        )

        item = str(input("Digite o item a ser deletado: ")).lower()

        lista = f.delete(lista, item)
        f.save_list(lista)