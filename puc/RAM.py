from puc.Memoria import Memoria


class RAM(Memoria):
    def __init__(self, W):
        super().__init__(W)  # Chama o construtor da classe base (Memoria) com a capacidade especificada (W)
        self.dados = [0] * W  # Inicializa uma lista de dados com tamanho W, preenchida com zeros

    def read(self, endereco):
        self.verifica_endereco(endereco)  # Chama o método verifica_endereco para garantir que o endereço seja válido
        return self.dados[endereco]  # Retorna o valor armazenado na posição de memória especificada pelo endereço

    def write(self, endereco, x):
        self.verifica_endereco(endereco)  # Chama o método verifica_endereco para garantir que o endereço seja válido
        self.dados[endereco] = x  # Escreve o valor x na posição de memória especificada pelo endereço
