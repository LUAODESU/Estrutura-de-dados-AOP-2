class No:
    """Representa um elemento da lista encadeada."""

    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None

    @property
    def valor(self):
        return self.__valor

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, no):
        self.__proximo = no


class Lista:
    """TAD para armazenamento dinâmico de inteiros usando nós encadeados."""

    def __init__(self):
        self.__inicio = None

    def inserir(self, valor):
        """Insere um valor inteiro no final da lista."""
        if type(valor) is not int:
            raise TypeError("O valor deve ser um inteiro.")

        novo = No(valor)

        if self.__inicio is None:
            self.__inicio = novo
            return

        atual = self.__inicio
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo

    def remover(self, valor):
        """Remove a primeira ocorrência do valor e informa o resultado."""
        if self.__inicio is None:
            return False

        if self.__inicio.valor == valor:
            self.__inicio = self.__inicio.proximo
            return True

        anterior = self.__inicio
        atual = self.__inicio.proximo

        while atual is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                return True

            anterior = atual
            atual = atual.proximo

        return False

    def buscar(self, valor):
        """Verifica se o valor está armazenado na estrutura."""
        atual = self.__inicio

        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo

        return False

    def destruir(self):
        """Remove a referência para o primeiro nó, esvaziando a estrutura."""
        self.__inicio = None
