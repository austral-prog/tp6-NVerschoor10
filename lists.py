

def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements
    longitud = len(lista)
    if longitud >= 6:
        del lista[5]
    longitud = len(lista)
    if longitud >= 5:
        del lista[4]
    longitud = len(lista)
    if longitud >= 1:
        del lista[0]
    return lista

def add_elements(list_to_add_elements):
    lista = list_to_add_elements
    lista.insert(0,"Pink")
    lista = lista+["Yellow"]
    return lista


def is_empty(list_to_check):
    lista = list_to_check
    longitud = len(lista)
    a = longitud == 0
    return a

def check_lists(list_to_compare1, list_to_compare2):
    lista1 = list_to_compare1
    lista2 = list_to_compare2
    long1 = len(lista1)
    long2 = len(lista2)
    if long1 >= 3 and long2 >=3:
        elemento1 = lista1[2:3]
        elemento2 = lista2[2:3]
        if elemento1 == elemento2:
            return True
        else:
            return False 
    else:
        return False
            


def list_of_lists(list_of_lists_to_modify):
    lista_madre = list_of_lists_to_modify
    lista1 = lista_madre[0]
    lista2 = lista_madre[1]
    lista3 = lista_madre[2]
    lista1 = lista1[0:2]
    lista2 = lista2[1:4]
    longitud = len(lista3)
    lista3 = lista3[longitud-2:longitud]
    lista_madre =[lista1,lista2,lista3]
    return lista_madre
