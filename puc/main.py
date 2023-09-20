from puc.CPU import CPU
from puc.Cache import Cache
from puc.EnderecoInvalido import EnderecoInvalido
from puc.IO import IO
from RAM import RAM

# Alunos: Dayane Ratzhe, Nicholas Zaze, Raphaela Vieira

print("Cache com Mapeamento Direto")
print()
try:

    io = IO(print)
    ram = RAM(11)  # 2K de RAM (2**11)
    cache = Cache(128, 16, ram) # total cache = 128, cacheline = 16 palavras
    cpu = CPU(io, cache)

    inicio = 0
    ram.write(inicio, 110)
    ram.write(inicio + 1, 130)
    cpu.run(inicio)
except EnderecoInvalido as e:
    print("Erro:", e)
