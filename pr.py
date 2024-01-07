# si tengo una lista de n elementos 

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

elements_by_divicion=6
aux = len(lista)/elements_by_divicion
if aux > int(aux):
    subdiviciones=int(aux)+1
else:
    subdiviciones=int(aux)

lista_2 = []
for i in range(subdiviciones):
    aux_list=[]
    for x in range(elements_by_divicion):
        try:
            initial_element = lista[0]
            lista.pop(0)
            print(lista)
            aux_list.append(initial_element)
        except IndexError:
            break
    lista_2.append(aux_list)

print(lista_2)

# y quiero q pase a 

lista2= [[1,2],[3,4],[5,6],[7,8],[9,10]]