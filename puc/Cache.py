from EnderecoInvalido import EnderecoInvalido
from Memoria import Memoria

class Cache(Memoria):
    def __init__(self, capacidade, tamCacheLine, ram):
        super().__init__(capacidade)  # Chama o construtor da classe base (Memoria) com a capacidade especificada
        self.ram = ram # Associa a RAM à cache
        self.dados = [[0] * (tamCacheLine + 1) for _ in range(capacidade)]  # Inicializa os dados da cache como uma matriz
        self.modificada = False  # Inicializa a flag modificada como False
        self.copy_line_from_ram(0, 0)  # Copia uma linha da RAM para a cache durante a inicialização

    def read(self, enderecoBit):
        print("READCACHE")  # Imprime uma mensagem de depuração
        resp = 0  # Inicializa a resposta como zero
        x = enderecoBit  # Atribui o endereçoBit à variável x
        print("x=" + bin(x))  # Imprime o valor de x em binário

        # # Declaração e extração de valores t, r, s e w a partir do endereçoBit
        w = x & 0b111111  # Extrai os 6 bits menos significativos de x
        print("w=" + bin(w))  # Imprime w em binário
        r = (x >> 6) & 0b1111111  # Extrai os 7 bits seguintes de x (deslocando 6 bits para a direita)
        print("r=" + bin(r))  # Imprime r em binário
        t = (x >> 12) & 0b11111111111  # Extrai os 11 bits mais significativos de x (deslocando 12 bits para a direita)
        print("t=" + bin(t))  # Imprime t em binário
        t_ = (self.dados[r][0] >> 18) & 0b11111111111  # Extrai a tag da posição r da cache
        print("t_=" + bin(t_))  # Imprime t_ em binário
        s = t_ | r | 0b000000  # Concatenação de t_, r e zeros para obter s
        print("s=" + bin(s))  # Imprime s em binário

        cache_hit = t == t_  # Verifica se houve cache hit comparando t com t_
        if cache_hit:
            resp = self.dados[r][w + 1]  # # Se houve cache hit, obtém o valor da cache tag = 0
        else:
            print("CacheMiss - End: " + str(x)) # Imprime uma mensagem indicando cache miss
            if self.modificada:
                self.copy_line_to_ram(s, r) # Se a cache estiver modificada, copia a linha para a RAM
                self.modificada = False  # Reseta a flag modificada
            self.copy_line_from_ram(s, r)  # Copia a linha da RAM para a cache
            resp = self.dados[r][w + 1]  # Obtém o valor da cache após a cópia


        print("resp=" + str(resp))  # Imprime a resposta
        return resp  # Retorna a resposta

    def write(self, enderecoBit, valor):
        x = enderecoBit  # Atribui o endereçoBit à variável x
        print("x=" + bin(x))  # Imprime o valor de x em binário
        t, r, s, w = 0, 0, 0, 0  # Inicializa t, r, s e w como zeros

        print("WRITE")  # Imprime uma mensagem de depuração

        # Declaração e extração de valores t, r, s e w a partir do endereçoBit
        w = x & 0b111111  # Extrai os 6 bits menos significativos de x
        print("w=" + bin(w))  # Imprime w em binário
        r = (x >> 6) & 0b111111111111  # Extrai os 12 bits seguintes de x (deslocando 6 bits para a direita)
        print("r=" + bin(r))  # Imprime r em binário
        t = (x >> 18) & 0b11111  # Extrai os 5 bits mais significativos de x (deslocando 18 bits para a direita)
        print("t=" + bin(t))  # Imprime t em binário
        t_ = (self.dados[r][0] >> 18) & 0b11111  # Extrai a tag da posição r da cache
        print("t_=" + bin(t_))  # Imprime t_ em binário
        s = t_ | r | 0b000000  # Concatenação de t_, r e zeros para obter s
        print("s=" + bin(s))  # Imprime s em binário


        cache_hit = t == t_ # Verifica se houve cache hit comparando t com t_
        if cache_hit:
            print("CACHEHIT")  # Se houve cache hit, imprime uma mensagem indicando cache hit
        else:
            print("CacheMiss - End: " + str(x))  # Imprime uma mensagem indicando cache miss
            if self.modificada:
                self.copy_line_to_ram(s, r)  # Se a linha da cache foi modificada, copia-a de volta para a RAM
                self.modificada = False  # Reseta o indicador de modificação da cache
            self.dados[r][w + 1] = valor  # Escreve o valor na cache na posição w (mais 1 para evitar a posição 0 que armazena a tag)

    def copy_line_to_ram(self, s, r):
        i = 0
        try:
            while i < self.capacidade:
                self.ram.write(s + i, self.dados[r][i])  # Copia a linha da cache de volta para a RAM.
                i += 1
        except EnderecoInvalido as e:
            while i < self.capacidade:
                self.ram.write(s + i, self.dados[r][i])  # Lida com exceção e tenta novamente a cópia.
                i += 1

    def copy_line_from_ram(self, s, r):
        i = 0
        try:
            while i < 64:
                self.dados[r][i] = self.ram.read(s << 6 | i)  # Copia uma nova linha da RAM para a cache (s concatenado com i).
                i += 1
        except EnderecoInvalido as e:
            while i < self.capacidade:
                self.dados[r][i] = self.ram.read(s << 6 | i)  # Lida com exceção e tenta novamente a cópia.
                i += 1