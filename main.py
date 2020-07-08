from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

#fila_teste = FilaNormal()
#fila_teste.atualizafila()
#fila_teste.atualizafila()
#fila_teste.atualizafila()
#print(fila_teste.chamacliente(12))
#print(fila_teste.chamacliente(13))

fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(14))
print(fila_teste2.chama_cliente(15))
print(fila_teste2.estatistica('10/01/1993', 197, 'detail'))
