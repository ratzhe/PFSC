class CPU:
    def __init__(self, es, mem):
        # Registradores da CPU
        self.PC = 0  # Inicializa o Program Counter (contador de programa) com 0
        self.rA = 0  # Inicializa o registrador A com 0
        self.rB = 0  # Inicializa o registrador B com 0
        self.rC = 0  # Inicializa o registrador C com 0
        self.mem = mem  # Atribui o objeto 'mem' (memória) passado como argumento ao atributo 'mem'
        self.es = es  # Atribui o objeto 'es' (saída) passado como argumento ao atributo 'es'

    def run(self, ender):
        print("ender=" + bin(ender))  # Imprime o valor do endereço em formato binário
        self.PC = ender  # Inicializa o Program Counter com o endereço 'ender'

        # Lê o "programa" da memória
        self.rA = self.mem.read(self.PC)  # Lê um valor da memória e armazena em 'rA'
        self.PC += 1  # Incrementa o Program Counter para apontar para o próximo endereço
        self.rB = self.mem.read(self.PC)  # Lê um valor da memória e armazena em 'rB'
        self.PC += 1  # Incrementa o Program Counter novamente

        # Executa o programa
        self.rC = 1  # Inicializa o registrador C (contador) com 1
        while self.rA <= self.rB:  # Escreve o valor de 'rB' na memória no endereço 'rA'
            self.mem.write(self.rA, self.rC)  # Escreve o valor de 'rC' na memória no endereço 'rA'
            self.es.output("> " + bin(self.rA) + " -> " + str(self.rC) + "\n")
            # Imprime uma mensagem indicando o endereço e o valor que está sendo escrito na memória
            self.rC += 1  # Incrementa o contador 'rC'
            self.rA += 1  # Incrementa 'rA' para avançar para o próximo endereço na memória