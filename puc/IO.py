class IO:
    def __init__(self, out):
        self.saida = out # Cria um atributo de instância chamado 'saida' e o inicializa com o objeto 'out' passado como argumento.

    def output(self, s):
        self.saida.print(s) # Imprime a string 's' diretamente no console (correção).
