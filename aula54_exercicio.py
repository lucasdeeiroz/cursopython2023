import os

lista_de_compras = []
print('Sua lista de compras está vazia')
print('Selecione uma opção')
opcao_escolhida = input('[i]nserir   [s]air: ')
while opcao_escolhida != 'S' or opcao_escolhida != 's':
    os.system('cls')
    if len(lista_de_compras) == 0:
        if opcao_escolhida == "I" or opcao_escolhida == "i":
            print('Sua lista de compras está vazia')
            item = input('Digite um item para adicionar à sua lista de compras: ')
            lista_de_compras.append(item)
            os.system('cls')
            for i, valor in enumerate(lista_de_compras):
                print(i+1, valor)
            print('Selecione uma opção')
            opcao_escolhida = input('[i]nserir   [a]pagar   [s]air: ')
        elif opcao_escolhida == "S" or opcao_escolhida == "s":
            break
        else:
            print('Sua lista de compras está vazia')
            print('Selecione uma opção válida')
            opcao_escolhida = input('[i]nserir   [s]air: ')
    else:
        if opcao_escolhida == "I" or opcao_escolhida == "i":
            for i, valor in enumerate(lista_de_compras):
                print(i+1, valor)
            item = input('Digite um item para adicionar à sua lista de compras: ')
            lista_de_compras.append(item)
            os.system('cls')
            for i, valor in enumerate(lista_de_compras):
                print(i+1, valor)
            print('Selecione uma opção')
            opcao_escolhida = input('[i]nserir   [a]pagar   [s]air: ')
        elif opcao_escolhida == "A" or opcao_escolhida == "a":
            for i, valor in enumerate(lista_de_compras):
                print(i+1, valor)
            item = input('Digite o numero de um item para apagar: ')
            os.system('cls')
            try:
                indice = int(item)
                del lista_de_compras[indice-1]
                print("Item removido")
            except:
                print("Opção inválida")
            for i, valor in enumerate(lista_de_compras):
                print(i+1, valor)
            print('Selecione uma opção')
            opcao_escolhida = input('[i]nserir   [a]pagar   [s]air: ')
        elif opcao_escolhida == "S" or opcao_escolhida == "s":
            break
        else:
            print('Sua lista de compras está vazia')
            print('Selecione uma opção válida')
            opcao_escolhida = input('[i]nserir   [a]pagar   [s]air: ')