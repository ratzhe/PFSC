class EnderecoInvalido(Exception):
    def __init__(self, e):
        super().__init__() # Chama o construtor da classe base 'Exception'
        self.ender = e # Armazena o endereço inválido como um atributo do objeto de exceção


    def __str__(self):
        return "Endereco " + str(self.ender) + " inválido." # Define a representação em string da exceção