import random
def desordena(lista,largo_de_lista,contador ):
    if contador<largo_de_lista:
        numero_Random =random.randint(contador,largo_de_lista-1)
        lista[contador],lista[numero_Random] = lista[numero_Random],lista[contador]
        desordena(lista,largo_de_lista,contador+1)
x=[1,2,3,4,5,6,7,8,9]
desordena(x,len(x),0)
print(x)