def numeroAPalabra(numero):

    if numero == 0:
        return 'cero'

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

    en_palabras = en_palabras.replace('dieciuno', 'once')
    en_palabras = en_palabras.replace('diecidos', 'doce')
    en_palabras = en_palabras.replace('diecitres', 'trece')
    en_palabras = en_palabras.replace('diecicuatro', 'catorce')
    en_palabras = en_palabras.replace('diecicinco', 'quince')

    if en_palabras.endswith('dieci'):
        en_palabras = en_palabras.replace('dieci', 'diez')
    elif en_palabras.endswith('veinti'):
        en_palabras = en_palabras.replace('veinti', 'veinte')
    elif en_palabras.endswith(' y'):
        en_palabras = en_palabras[:-2]
    elif en_palabras.endswith('ciento'):
        en_palabras = en_palabras.replace('ciento', 'cien')

    return en_palabras.capitalize()


valor = 670
print('Numero ingresado: ', valor)
print(numeroAPalabra(valor))
