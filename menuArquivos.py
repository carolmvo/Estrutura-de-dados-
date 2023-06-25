


def menu_internoArquivos():
    while True:
        print("Arquivos:")
        print("Escolha uma opção: ")
        print("1. Lista desordenada grande")
        print("2. Lista desordenada pequena")
        print("3. Lista ordenada grande")
        print("4. Lista ordenada pequena")
        print("5. Matriz 5x5")
        print("6. Matriz 3x3")
        print("7. Escolha outro arquivo")
        print("8. Voltar ao menu principal")
        selecaoArquivo = input("Escolha uma opção: ")
       
        
        if selecaoArquivo == '1': 
            with open('./txt/arquivo desordenado grande.txt', 'r') as arquivo:
                num = arquivo.read()
            valoresDesordenadoGrande = num.split(',')
            array = [int(valor.strip()) for valor in valoresDesordenadoGrande]
            return array
        elif selecaoArquivo == '2':
            with open('./txt/arquivo desordenado pequeno.txt', 'r') as arquivo:
                num = arquivo.read()
            valoresDesordenadoPequeno = num.split(',')
            array = [(valor.strip()) for valor in valoresDesordenadoPequeno]
            return array
        elif selecaoArquivo == '3':
            with open('./txt/arquivo ordenado grande.txt', 'r') as arquivo:
                num = arquivo.read()
            valoresOrdenadoGrande = num.split(',')
            array = [int(valor.strip()) for valor in valoresOrdenadoGrande]
            return array
        elif selecaoArquivo == '4':
            with open('./txt/arquivo ordenado pequeno.txt', 'r') as arquivo:
                num = arquivo.read()
            valoresOrdenadoPequeno = num.split(',')
            array = [int(valor.strip()) for valor in valoresOrdenadoPequeno]
            return array
        elif selecaoArquivo == '5':
            array = ('./txt/matriz 5x5.txt')
            return array
        elif selecaoArquivo == '6':
            array = ('./txt/matriz 3x3.txt')
            return array
        elif selecaoArquivo == '7':
            while True:
                i = input("É uma matriz? 1- sim 2- não 3- cancelar")
                caminho_arquivo = input("Digite o caminho de diretório que o arquivo se encontra: ")
                if i == '1':
                    array = caminho_arquivo
                    return array
                elif i == '2':
                    with open(caminho_arquivo, 'r') as arquivo:
                        num = arquivo.read()
                    valoresNovos = num.split(',')
                    array = [int(valor.strip()) for valor in valoresNovos]
                    return array
                elif i == '3':
                    print("Voltando ao menu principal")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
                return True
        elif selecaoArquivo == '8':
            print("Voltando ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True