"""
1. Crear una función que pase de entero > 0 y < 4.000 a romano
2. Cualquier otra entrada debe dar error


"""

class RomanNumerError(Exception):
    pass

numero_romano = (
    (1000, 'M'), (500, 'D'), (100, 'C'), (50, 'D'), (10, 'X'), (5, 'V'), (1, 'I')
)

centenas = (
    (100, 'C'), (200, 'CC'), (300, 'CCC'), (400, 'CD'), (500, 'D'),
     (600, 'DC'), (700, 'DCC'), (800, 'DCCC'), (900, 'CM')) 

decenas = ((10, 'X'), (20, 'XX'), (30, 'XXX'), (40, 'XL'), (50, 'L'),
     (60, 'LX'), (70, 'LXX'), (80, 'LXXX'), (90, 'XC'))

unidades = ((1, 'I'), (20, 'II'), (30, 'III'), (40, 'IL'), (50, 'V'),
     (60, 'VI'), (70, 'VII'), (80, 'VIII'), (90, 'IX'))

def entero_a_romano(numero):
"""
numero = str(numero)
    longitud = len(numero)
    
    if longitud < 4:
        numero ="{:0>4s}".format(numero)
"""
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)
    
    ix = 0
    longitud = 4

    for n in numero:
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        ix += 1
    return digitos
