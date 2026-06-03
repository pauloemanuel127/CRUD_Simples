import functions as f

# Definindo o lista como vazia e começando as funções

lista = None

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
        break

    elif entrada == "1":

        print(
            "Digite o item a ser inserido no estoque" \
            " e na linha seguinte digite a quantidade"
        ) 

        item = str(input()).lower()
        quantidade = int(input())

        lista = f.append(lista, item, quantidade)
    
    elif entrada == "2":

        print(
            "Digite o item a ser verificado."
        )

        item = str(input()).lower()

        f.read(lista, item)

    elif entrada == "3":
        
        print(
            "Digite o item a ser alterado, o novo item que sera alocado" \
            " (caso não tenha novo item apenas deixe em branco [aperte Enter])" \
            "e a nova quantidade" \
            " (caso não tenha nova quantidade digite -1)"
        )

        item = str(input()).lower()
        novo_item = str(input()).lower()
        nova_quantidade = input()

        while not f.validar(nova_quantidade):
            nova_quantidade = input()

        lista = f.update(lista, item, novo_item, int(nova_quantidade))
    
    elif entrada == "4":

        print(
            "Digite o item a ser deletado," \
            " lembrando que a quantidade será deletada também"
        )

        item = str(input()).lower()

        lista = f.delete(lista, item)