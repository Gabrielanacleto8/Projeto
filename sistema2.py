# Sistema de cadastro de produtos
produtos = []

def mostrar_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU ---")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Editar produto")
    print("4. Remover produto")
    print("5. Sair")

def adicionar_produto():
    """Solicita os dados e adiciona um novo produto à lista."""
    print("\n--- ADICIONAR PRODUTO ---")
    try:
        nome = input("Nome do produto: ")
        # Validação básica para o nome
        if not nome.strip():
            print("O nome do produto não pode ser vazio.")
            return

        # Tentativa de converter para float (preço) e int (quantidade)
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade: "))

        if preco < 0 or quantidade < 0:
            print("Preço e quantidade não podem ser negativos.")
            return

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("Entrada inválida. Certifique-se de que o preço é um número e a quantidade é um número inteiro.")

def listar_produtos():
    """Exibe a lista de todos os produtos cadastrados."""
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    print("\n--- LISTA DE PRODUTOS ---")
    for i, produto in enumerate(produtos):
        # Exibe o número, nome, preço formatado com 2 casas decimais e quantidade.
        print(f"{i + 1}. {produto['nome']} | R${produto['preco']:.2f} | Quantidade: {produto['quantidade']}")

def editar_produto():
    """Permite ao usuário modificar as informações de um produto existente."""
    listar_produtos()
    if not produtos:
        return
    
    print("\n--- EDITAR PRODUTO ---")
    try:
        # Solicita o número do produto (mostrado na listagem, que começa em 1)
        indice = int(input("Digite o número do produto para editar: ")) - 1
        
        if 0 <= indice < len(produtos):
            produto_atual = produtos[indice]
            print(f"Editando: {produto_atual['nome']} (R${produto_atual['preco']:.2f}, Qtde: {produto_atual['quantidade']})")
            
            # Pede novos valores, o usuário pode apertar Enter para manter o atual
            nome = input(f"Novo nome (atual: {produto_atual['nome']}) [Enter para manter]: ")
            preco = input(f"Novo preço (atual: R${produto_atual['preco']:.2f}) [Enter para manter]: ")
            quantidade = input(f"Nova quantidade (atual: {produto_atual['quantidade']}) [Enter para manter]: ")

            if nome:
                produto_atual['nome'] = nome
            
            if preco: 
                # Converte o novo preço para float e atualiza
                produto_atual['preco'] = float(preco)
            
            if quantidade:
                # CORREÇÃO: Converte a nova quantidade para int e atualiza o campo 'quantidade'
                produto_atual['quantidade'] = int(quantidade)
            
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError: 
        print("Entrada inválida. Certifique-se de usar números para o índice, preço e quantidade.")

def remover_produto():
    """Remove um produto da lista com base no número."""
    listar_produtos()
    if not produtos:
        return
    
    print("\n--- REMOVER PRODUTO ---")
    try:
        # Solicita o número do produto (mostrado na listagem, que começa em 1)
        indice = int(input("Digite o número do produto para remover: ")) - 1
        
        if 0 <= indice < len(produtos):
            removido = produtos.pop(indice)
            print(f"Produto '{removido['nome']}' removido com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError: 
        print("Entrada inválida. Digite um número para o índice.")
        
# Loop principal do programa
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2': 
            listar_produtos()
        elif opcao == '3':
            editar_produto() 
        elif opcao == '4':
            remover_produto()
        elif opcao == '5':
            print("Encerrando programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")