""" Calculadora com while """
numero_1 = input('Digite um número: ')
operador = input('Digite o operador (+-/*): ')
numero_2 = input('Digite outro número: ')
resultado = 0
operadores_permitidos = '+-/*'

while True:
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        resultado = num_1_float + num_2_float
        print(f'{num_1_float}+{num_2_float}=', resultado)
    elif operador == '-':
        resultado = num_1_float - num_2_float
        print(f'{num_1_float}-{num_2_float}=', resultado)
    elif operador == '/':
        resultado = num_1_float / num_2_float
        print(f'{num_1_float}/{num_2_float}=', resultado)
    elif operador == '*':
        resultado = num_1_float * num_2_float
        print(f'{num_1_float}*{num_2_float}=', resultado)
    else:
        
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    while sair is False:
        operador = input('Digite o operador (+-/*): ')
        numero_2 = input('Digite outro número: ')
        num_1_float = resultado
        try:
            num_2_float = float(numero_2)
            numeros_validos = True
        except:
            numeros_validos = None

        if numeros_validos is None:
            print('Um ou ambos os números digitados são inválidos.')
            continue

        if operador not in operadores_permitidos:
            print('Operador inválido.')
            continue

        if len(operador) > 1:
            print('Digite apenas um operador.')
            continue

        print('Realizando sua conta. Confira o resultado abaixo:')

        if operador == '+':
            resultado = num_1_float + num_2_float
            print(f'{num_1_float}+{num_2_float}=', resultado)
        elif operador == '-':
            resultado = num_1_float - num_2_float
            print(f'{num_1_float}-{num_2_float}=', resultado)
        elif operador == '/':
            resultado = num_1_float / num_2_float
            print(f'{num_1_float}/{num_2_float}=', resultado)
        elif operador == '*':
            resultado = num_1_float * num_2_float
            print(f'{num_1_float}*{num_2_float}=', resultado)
        else:
        
            print('Nunca deveria chegar aqui.')

        sair = input('Quer sair? [s]im: ').lower().startswith('s')

        if sair is True:
            break
    break
