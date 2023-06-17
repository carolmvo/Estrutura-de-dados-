import sys
sys.path.append('./Ordenacao')
sys.path.append('./Pesquisa')


#Tratamento dos dados
    #Desordenado
with open('./txt/arquivo desordenado grande.txt', 'r') as arquivo:
    conteudoDesordenadoGrande = arquivo.read()

valoresDesordenadoGrande = conteudoDesordenadoGrande.split(',')
listaNumericaDesordenadoGrande = [int(valor.strip()) for valor in valoresDesordenadoGrande]

with open('./txt/arquivo desordenado grande positivo.txt', 'r') as arquivo:
    conteudoDesordenadoGrandePositivo = arquivo.read()

valoresDesordenadoGrandePositivo = conteudoDesordenadoGrandePositivo.split(',')
listaNumericaDesordenadoGrandePositivo = [int(valor.strip()) for valor in valoresDesordenadoGrandePositivo]

with open('./txt/arquivo desordenado grande negativo.txt', 'r') as arquivo:
    conteudoDesordenadoGrandeNegativo = arquivo.read()

valoresDesordenadoGrandeNegativo = conteudoDesordenadoGrandeNegativo.split(',')
listaNumericaDesordenadoGrandeNegativo = [int(valor.strip()) for valor in valoresDesordenadoGrandeNegativo]

with open('./txt/arquivo desordenado pequeno.txt', 'r') as arquivo:
    conteudoDesordenadoPequeno = arquivo.read()

valoresDesordenadoPequeno = conteudoDesordenadoPequeno.split(',')
listaNumericaDesordenadoPequeno = [int(valor.strip()) for valor in valoresDesordenadoPequeno]

with open('./txt/arquivo desordenado pequeno positivo.txt', 'r') as arquivo:
    conteudoDesordenadoPequenoPositivo = arquivo.read()

valoresDesordenadoPequenoPositivo = conteudoDesordenadoPequenoPositivo.split(',')
listaNumericaDesordenadoPequenoPositivo = [int(valor.strip()) for valor in valoresDesordenadoPequenoPositivo]

with open('./txt/arquivo desordenado pequeno negativo.txt', 'r') as arquivo:
    conteudoDesordenadoPequenoNegativo = arquivo.read()

valoresDesordenadoPequenoNegativo = conteudoDesordenadoPequenoNegativo.split(',')
listaNumericaDesordenadoPequenoNegativo = [int(valor.strip()) for valor in valoresDesordenadoPequenoNegativo]

    #Ordenado
with open('./txt/arquivo ordenado grande.txt', 'r') as arquivo:
    conteudoOrdenadoGrande = arquivo.read()

valoresOrdenadoGrande = conteudoOrdenadoGrande.split(',')
listaNumericaOrdenadoGrande = [int(valor.strip()) for valor in valoresOrdenadoGrande]

with open('./txt/arquivo ordenado grande positivo.txt', 'r') as arquivo:
    conteudoOrdenadoGrandePositivo = arquivo.read()

valoresOrdenadoGrandePositivo = conteudoOrdenadoGrandePositivo.split(',')
listaNumericaOrdenadoGrandePositivo = [int(valor.strip()) for valor in valoresOrdenadoGrandePositivo]

with open('./txt/arquivo ordenado grande descendente negativo.txt', 'r') as arquivo:
    conteudoOrdenadoGrandeNegativo = arquivo.read()

valoresOrdenadoGrandeNegativo = conteudoOrdenadoGrandeNegativo.split(',')
listaNumericaOrdenadoGrandeNegativo = [int(valor.strip()) for valor in valoresOrdenadoGrandeNegativo]

with open('./txt/arquivo ordenado pequeno.txt', 'r') as arquivo:
    conteudoOrdenadoPequeno = arquivo.read()

valoresOrdenadoPequeno = conteudoOrdenadoPequeno.split(',')
listaNumericaOrdenadoPequeno = [int(valor.strip()) for valor in valoresOrdenadoPequeno]

with open('./txt/arquivo ordenado pequeno positivo.txt', 'r') as arquivo:
    conteudoOrdenadoPequenoPositivo = arquivo.read()

valoresOrdenadoPequenoPositivo = conteudoOrdenadoPequenoPositivo.split(',')
listaNumericaOrdenadoPequenoPositivo = [int(valor.strip()) for valor in valoresOrdenadoPequenoPositivo]

with open('./txt/arquivo ordenado pequeno descendente negativo.txt', 'r') as arquivo:
    conteudoOrdenadoPequenoNegativo = arquivo.read()

valoresOrdenadoPequenoNegativo = conteudoOrdenadoPequenoNegativo.split(',')
listaNumericaOrdenadoPequenoNegativo = [int(valor.strip()) for valor in valoresOrdenadoPequenoNegativo]