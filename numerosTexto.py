def numeroAPalabra(numero):
    en_palabras = ''

    unidades = ['', 'uno', 'dos', 'tres', 'cuatro',
                'cinco', 'seis', 'siete', 'ocho', 'nueve']

    decenas = ['', 'dieci', 'veinti', 'treinta y ', 'cuarenta y ',
               'cincuenta y ', 'sesenta y ', 'setenta y ', 'ochenta y ', 'noventa y ']

    centenas = ['', 'ciento ', 'doscientos ', 'trescientos ', 'cuatrocientos ',
                'quinientos ', 'seiscientos ', 'setecientos ', 'ochocientos ', 'novecientos ']

    numero = '0' * (3 - len(str(numero))) + str(numero)

    unidad = int(numero[-1])
    decena = int(numero[-2])
    centena = int(numero[-3])

    en_palabras = '{}{}{}'.format(
        centenas[centena], decenas[decena], unidades[unidad]).strip()

    return en_palabras


valor = 111
print('Numero ingresado: ', valor)
print(numeroAPalabra(valor))
