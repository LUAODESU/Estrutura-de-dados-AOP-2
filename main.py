from lista import Lista


def exibir_resultado(mensagem, resultado):
    print(f"{mensagem}: {'Sucesso' if resultado else 'Falha'}")


def main():
    # 1. Criar a estrutura
    lista = Lista()
    print("Lista criada e inicializada vazia.")

    # 2. Inserir elementos
    print("\nInserindo elementos...")
    lista.inserir(10)
    lista.inserir(20)
    lista.inserir(30)
    lista.inserir(20)
    print("Valores inseridos: 10, 20, 30, 20")

    # 3. Buscar elementos
    print("\nBuscando elementos...")
    exibir_resultado("Buscar 20", lista.buscar(20))
    exibir_resultado("Buscar 99", lista.buscar(99))

    # 4. Remover elementos
    print("\nRemovendo elementos...")
    exibir_resultado("Remover primeira ocorrência de 20", lista.remover(20))
    exibir_resultado("Remover 99", lista.remover(99))

    # 5. Verificar novamente após a remoção
    print("\nVerificando a estrutura após a remoção...")
    exibir_resultado("Buscar 20", lista.buscar(20))

    # 6. Destruir a estrutura
    print("\nDestruindo a estrutura...")
    lista.destruir()
    exibir_resultado("Buscar 10 após destruir", lista.buscar(10))

    print("\nPrograma executado com sucesso.")


if __name__ == "__main__":
    main()
