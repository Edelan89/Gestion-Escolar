def calculoPromedio(lista):
    
    int_lista = []
    
    for elements in lista:
        int_lista.append(float(elements))
    
    # if len(lista) == 0:
    #     return 0
    suma = sum(int_lista)
    promedio = suma/len(int_lista)
    return promedio

#------------------ Prueba -------------------
#listaPrueba = []
#print(calculoPromedio(listaPrueba))
