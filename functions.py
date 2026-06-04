# ===============[SIMPLE CRUD WITH LINKED LIST]===============

# ===============[CREATE]===============

def create_node(item, quantidade):
    """
    Essa função recebe o item e a quantidade e gera o novo elemento na lista encadeada, 
    colocando-o no nó. Retorna o novo elemento.
    """

    return {'item': item, 'quantidade': quantidade, 'proximo': None}

def append(head, item, quantidade):
    """
    Essa função recebe a lista, o item a ser adicionado e a quantidade,
    com isso adiciona o novo elemento na lista.
    Retorna a lista com o novo elemento.
    """

    new_node = create_node(item, quantidade)

    if head is None:
        print("\nItem adicionado com sucesso.\n")
        return new_node
    
    current = head

    while current['proximo'] is not None:
        current = current['proximo']

    current['proximo'] = new_node
    print("\nItem adicionado com sucesso.\n")
    return head

# ===============[READ]=============== 

def read(head, target):
    """
    Essa função recebe a lista e o item a ser procurado, e exibe se o item foi encontrado,
    se o item for encontrado ele exibe uma mensagem informando a quantidade do item.
    Quando o item é encontrado retorna True, quando não é retorna False.
    """

    current = head

    while current is not None:

        if current['item'] == target:
            print(f"\nItem encontrado, você possui {current['quantidade']} {target}s.\n")
            return True
        
        current = current['proximo']
    
    print("\nItem não encontrado, tente novamente.\n")
    return False

# ===============[UPDATE]===============

def update(head, item, novo_item, nova_quantidade):
    """
    Essa função recebe a lista, o elemento desejado a ser realizada a mudança e os novos valores,
    realiza a busca linear do valor desejado, quando encontrado faz a alteração do item ou de sua quantidade,
    quando o item não é encontrado informa que o item não foi encontrado.
    Retorna a lista alterada quando o item é encontrado, quando não retorna a lista da forma que estava.
    """

    current = head

    while current is not None:

        if current['item'] == item:
            
            if novo_item != "":
                current['item'] = novo_item
            
            if nova_quantidade != -1:
                current['quantidade'] = nova_quantidade
            
            print("\nItem atualizado com sucesso.\n")
            return head
           
        current = current['proximo']
    
    print("\nItem não encontrado.\n")
    return head

# ===============[DELETE]===============

def delete(head, item):
    """
    Essa função recebe a lista e o item desejado a ser excluido,
    verifica se a lista está vazia caso não esteja, procura o elemento desejado,
    se for encontrado deleta o elemento, se não informa que o elemento não foi encontrado.
    Retorna None caso a lista seja vazia, retorna a lista sem o elemento desejado caso ele seja encontrado,
    retorna a lista normal caso o elemento não seja encontrado.
    """

    if head is None:
        print("\nA lista está vazia.\n")
        return None
    
    if head['item'] == item:
        print("\nItem removido com sucesso.\n")
        return head['proximo']
    
    current = head

    while current['proximo'] is not None:

        if current['proximo']['item'] == item:
            current['proximo'] = current['proximo']['proximo']
            print("\nItem removido com sucesso.\n")
            return head
        
        current = current['proximo']

    print("\nItem não encontrado.\n")
    return head

# ===============[Validate]===============

def validar(valor):
    """
    Essa função é responsavel por verificar se o valor digitado na chamada update é valido.
    Quando é valido retorna True, quando é invalido em alguma das condições retorna False.
    """

    try:
        temp = int(valor)

    except ValueError:
        return False

    if int(valor) >= -1:
        return True
    
    else: 
        return False

# ===============[Save_List]===============

def save_list(head):
    """
    Essa função salva os elementos atuais da lista encadeada em um arquivo.
    Retorna None.
    """
    current = head

    with open("list.txt", "w", encoding="utf-8") as arquivo:

        while current is not None:

            arquivo.write(f"{current['item']}, {current['quantidade']}\n")
            current = current['proximo']
        return

# ===============[Load_List]===============
def load_list():
    """
    Essa função carrega os dados do arquivo TXT devolta para a lista encadeada,
    ela verifica se o arquivo exista, caso não mantém a lista vazia, 
    se o arquivo existir verifica se tem algum elemento, se tiver carrega na lista,
    se não mantem a lista vazia.
    A função retorna sempre a lista.
    """
    lista = None

    def add(lista, item, quantidade):
        """
        Essa função é idêntica à função de append, 
        porém foi criada para ser utilizada apenas nessa circunstancia,
        não exibe nenhuma mensagem.
        Retorna a lista com o novo elemento.
        """
        new_node = create_node(item, quantidade)

        if lista is None:
            return new_node
        
        current = lista

        while current['proximo'] is not None:
            current = current['proximo']

        current['proximo'] = new_node
        return lista
    
    try:

        with open("list.txt", "r") as arquivo:

            linhas = arquivo.readlines()

            for linha in linhas:

                valores = linha.split(", ")
                item = valores[0]
                quantidade = int(valores[1])
              
                lista = add(lista, item, quantidade)
            return lista
    
    except FileNotFoundError:
        return lista