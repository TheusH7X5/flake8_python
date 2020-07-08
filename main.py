#from fila_normal import FilaNormal
#from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

#fila_teste = FilaNormal()
#fila_teste.atualizafila()
#fila_teste.atualizafila()
#fila_teste.atualizafila()
#print(fila_teste.chamacliente(12))
#print(fila_teste.chamacliente(13))

#fila_teste2 = FilaNormal()
#fila_teste2.atualiza_fila()
#fila_teste2.atualiza_fila()
#fila_teste2.atualiza_fila()
#print(fila_teste2.chama_cliente(14))
#print(fila_teste2.chama_cliente(15))
#print(fila_teste2.estatistica('10/01/1993', 215, 'detail'))

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(11))
print(teste_fabrica.chama_cliente(12))
print(teste_fabrica.estatistica(EstatisticaDetalhada('20/03/2025', 120)))
