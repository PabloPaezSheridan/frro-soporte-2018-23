
# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    numeros=[0,1,2,3,4,5,6,7,8,9]
    lon= len(lista)

    for i in range(lon):
        print("for lista")
        j=0
        while j<= len(numeros):
            print("for numeros")
            if lista[i]==j:
                lista.append(lista[i])
                lista.pop(i)
                break
            j=j+1    
    return lista

lista = ["n",0,"p",1]
print (numeros_al_final(lista))
   
