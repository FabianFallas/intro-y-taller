### DEterminar el valor promedio de la suma de los valores de una matriz

def valorpromedio(matriz):
    if isinstance (matriz, list) and matriz != []: #matriz diferente a lista vacia
        return valorpromedio_aux (matriz, 0, 0, 0 )
    else:
        return "ERROR"

def valorpromedio_aux (matriz, fila,columna, resultado):
    if fila >= len (matriz) :
        return resultado // (len (matriz) * len(matriz[0]))
    elif columna == len(matriz[0]):
        return valorpromedio_aux (matriz, fila +1, 0, resultado )
    else:
        return valorpromedio_aux (matriz, fila, columna + 1, resultado + matriz[fila] [columna] )
    
