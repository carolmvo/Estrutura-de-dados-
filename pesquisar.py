import sys
sys.path.append('./Ordenacao')
sys.path.append('./Pesquisa')
# import NOT_FOUND
import buscaEmDesordenacao
import buscaEmOrdenacao
import pesquisaBinaria
import pesquisaSequencial
from troca import swap
from tratamentoDados import *


#Pesquisa
    #Em Lista Desordenada
buscaDesordenadaGrande = str(buscaEmDesordenacao.find(listaNumericaDesordenadoGrande, 839))
with open('./resultado/buscaEmDesordenacao/resultadoBuscaDesordenadoGrande.txt', 'w') as arquivo:
    arquivo.write(buscaDesordenadaGrande)

    #Em Lista Ordenada
buscaOrdenadaGrande = str(buscaEmOrdenacao.scan(listaNumericaOrdenadoGrande, 66))
with open('./resultado/buscaEmOrdenacao/resultadoBuscaOrdenadoGrande.txt', 'w') as arquivo:
    arquivo.write(buscaOrdenadaGrande)


    #Busca binária
buscaBinaria = str(pesquisaBinaria.iterativeBinarySearch(listaNumericaOrdenadoGrande, 66))
with open('./resultado/buscaBinaria/resultadoBuscaBinariaGrande.txt', 'w') as arquivo:
    arquivo.write(buscaBinaria)


    #Busca sequencial
buscaSequencial = str(pesquisaSequencial.scanSequencial(listaNumericaOrdenadoGrande, 66))
with open('./resultado/buscaSequencial/resultadoBuscaSequencialGrande.txt', 'w') as arquivo:
    arquivo.write(buscaSequencial)