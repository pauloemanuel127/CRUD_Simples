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
        print("Item adicionado com sucesso.")
        return new_node
    
    current = head

    while current['proximo'] is not None:
        current = current['proximo']

    current['proximo'] = new_node
    print("Item adicionado com sucesso.")
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
            print(f"Item encontrado, você possui {current['quantidade']} {target}s.")
            return True
        
        current = current['proximo']
    
    print("Item não encontrado, tente novamente.")
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
            
            print("Item atualizado com sucesso.")
            return head
           
        current = current['proximo']
    
    print("Item não encontrado.")
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
        print("A lista está vazia.")
        return None
    
    if head['item'] == item:
        print("Item removido com sucesso.")
        return head['proximo']
    
    current = head

    while current['proximo'] is not None:

        if current['proximo']['item'] == item:
            current['proximo'] = current['proximo']['proximo']
            print("Item removido com sucesso.")
            return head
        
        current = current['proximo']

    print("Item não encontrado.")
    return head

# ===============[Validate]==============

def validar(valor):

    try:
        temp = int(valor)

    except ValueError:
        return False

    if int(valor) >= -1:
        return True
    
    else: return False