from puc.EnderecoInvalido import EnderecoInvalido


class Memoria:
    def __init__(self, capacidade):
        self.capacidade = capacidade # Inicializa a capacidade da memória com o valor especificado

    def verifica_endereco(self, endereco):
        # Verifica se o endereço está dentro dos limites da capacidade da memória
        if endereco < 0 or endereco >= self.capacidade:
            raise EnderecoInvalido(endereco)  # Lança a exceção 'EnderecoInvalido' se o endereço for inválido

    def read(self, endereco):
        pass  # Este método deve ser implementado nas subclasses para ler um valor na memória

    def write(self, endereco, valor):
        pass  # Este método deve ser implementado nas subclasses para escrever um valor na memória