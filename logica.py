import random

FILAS = 4
COLUMNAS = 4
FICHA_GANADORA = 2048
FICHAS_RANDOM = (2, 2, 4) #66% de probabilidades de que salga un 2
ARRIBA = 'w'
ABAJO = 's'
DERECHA = 'd'
IZQUIERDA = 'a'
MOVIMIENTOS = (ARRIBA, ABAJO, DERECHA, IZQUIERDA)

def inicializar_juego():
    '''Crea una matriz de dimensión COLUMNAS * FILAS,
    y la completa con valores 0 y dos randoms'''
    tablero = []                          #Lista de filas
    for i in range(FILAS):
        lista_fila = []                   #Lista de columnas
        for j in range(COLUMNAS):
            lista_fila.append(0)
        tablero.append(lista_fila)
    for random in range(2):     #Se añaden dos numeros random
        tablero = insertar_nuevo_random(tablero)
    return tablero

def mostrar_juego(tablero):
    '''Muestra por pantalla el tablero de juego'''
    for i in range(len(tablero)):
        print('.' * 7 * COLUMNAS)
        for j in range(len(tablero[0])):
            if tablero[i][j] == 0:
                print(f'|    ' + ' ', end = ' ')
            elif tablero[i][j] < 10:            #Si el número es de un dígito
                print(f'|    {tablero[i][j]}', end = ' ')
            elif tablero[i][j] < 100:           #Si el número es de dos dígitos
                print(f'|   {tablero[i][j]}', end = ' ')
            elif tablero[i][j] < 1000:          #Si el número es de tres dígitos
                print(f'|  {tablero[i][j]}', end = ' ')
            elif tablero[i][j] < 10000:         #Si el número es de cuatro dígitos
                print(f'| {tablero[i][j]}', end = ' ')
        print('|')
    print('.' * 7 * COLUMNAS)

def juego_ganado(tablero):
    '''Recorre el tablero y determina si hay
    una posición con el valor FICHA_GANADORA'''
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == FICHA_GANADORA:
                return True
    return False

def juego_perdido(tablero):
    '''Recorre el tablero y determina si ya no
    quedan espacios y/o combinaciones disponibles'''
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 0:          #Verifica si hay espacios vacíos
                return False
    for movimiento in MOVIMIENTOS:          #Verifica si hay movimientos disponibles
        if tablero != actualizar_juego(tablero, movimiento):
            return False
    return True

def pedir_direccion(tablero):
    '''Pide al jugador que realice un movimiento'''
    while True:
        direccion = input(f'Elegí una dirección ({ARRIBA}, {IZQUIERDA}, {ABAJO}, {DERECHA}): ')
        if direccion.lower() in MOVIMIENTOS:            #Verifica que sea una entrada válida
            return direccion
        print('Dirección inválida, intentá otra vez')

def actualizar_juego(tablero, direccion):
    '''Devuelve un nuevo tablero modificado según
    el movimiento realizado por el jugador'''
    tablero_nuevo = tablero[:]
    if direccion == ARRIBA or direccion == ABAJO:
        tablero_nuevo = trasponer_tablero(tablero_nuevo)
    if direccion == ABAJO or direccion == DERECHA:
        tablero_nuevo = invertir_filas(tablero_nuevo)
    tablero_nuevo = combinar_filas(tablero_nuevo)
    if direccion == ABAJO or direccion == DERECHA:
        tablero_nuevo = invertir_filas(tablero_nuevo)
    if direccion == ARRIBA or direccion == ABAJO:
        tablero_nuevo = trasponer_tablero(tablero_nuevo)
    return tablero_nuevo

def trasponer_tablero(tablero):
    '''Traspone el tablero, las columnas
    pasan a ser filas, y viceversa'''              #Para los movimientos ARRIBA y ABAJO
    tablero_traspuesto = []
    for j in range(len(tablero[0])):
        nueva_fila = []
        for i in range(len(tablero)):
            nueva_fila.append(tablero[i][j])
        tablero_traspuesto.append(nueva_fila)
    return tablero_traspuesto

def invertir_filas(tablero):
    '''Invierte las filas del tablero'''           #Para los movimientos ABAJO y DERECHA
    tablero_inverso = []
    for i in range(len(tablero)):
        fila_inversa = list(reversed(tablero[i]))
        tablero_inverso.append(fila_inversa)
    return tablero_inverso

def combinar_filas(tablero):
    '''Tras realizar un movimiento, combina las
    filas sumando los valores correspondientes'''
    tablero_combinado = []                  #Nuevo tablero combinado
    for i in range(len(tablero)):
        filas_combinadas = []               #Filas sin los espacios vacíos
        for j in range(len(tablero[i])):
            if tablero[i][j] != 0:
                filas_combinadas.append(tablero[i][j])

        for k in range(len(filas_combinadas) - 1):      #Se combinan las filas
            if filas_combinadas[k] == filas_combinadas[k + 1]:
                filas_combinadas[k] += filas_combinadas[k + 1]
                filas_combinadas[k + 1] = 0
        for m in filas_combinadas:
            if m == 0:
                filas_combinadas.remove(m)      #Se eliminan los ceros intermedios

        espacios_vacios = len(tablero[0]) - len(filas_combinadas)
        for espacios in range(espacios_vacios):
            filas_combinadas.append(0)          #Se agregan ceros al final
        tablero_combinado.append(filas_combinadas)
    return tablero_combinado

def insertar_nuevo_random(tablero):
    '''Elige una posicion vacía random e inserta
    un valor random entre FICHAS_RANDOM'''
    tablero_nuevo = []                  #Se crea un tablero nuevo
    lista_de_espacios = []              #Indices de los espacios vacíos
    for i in range(len(tablero)):
        filas_nuevas = []
        for j in range(len(tablero[0])):
            filas_nuevas.append(tablero[i][j])
            if tablero[i][j] == 0:
                lista_de_espacios.append((i, j))
        tablero_nuevo.append(filas_nuevas)
    i, j = random.choice(lista_de_espacios)               #Elige ubicación random
    tablero_nuevo[i][j] = random.choice(FICHAS_RANDOM)    #Elige número random entre FICHAS_RANDOM
    return tablero_nuevo
