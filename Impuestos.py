# Calculadora para calcular los impuestos de los juegos de steam

while True:
    def Impuestos():
        constante = float(1.75)
        dato = float(input('Ingresa el precio del juego que deseas calcular (pesos ARG): '))
        resultado = str(dato * constante)
        print('El precio del juego con impuestos aplicados es de: ' + resultado) 

    value = str(input('Usted desea ejecutar la calculadora?: '))

    if(value == 'si' or value == 'Si' or value == 'SI'):
        Impuestos()
    else:
        print('Bueno, nv B)')
        break