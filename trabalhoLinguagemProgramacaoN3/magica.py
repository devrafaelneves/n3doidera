# vamos printar 3 listas 

a = ['a1','a2', 'a3', 'a4', 'a5', 'a6', 'a7']
b = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7']
c = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']

# print (a[0]+b[0]+c[0])

lista = a + b + c
# print (lista)

for i in range (7):

    print(a[i] + ' ' + b[i] + ' ' + c[i])

resposta = (input('Escolha um termo e digite em qual fileira está (a, b ou c) '))


if (resposta=='a'):

    lista = b+a+c
   
if (resposta=='c'):

    lista = a+c+b

if(resposta=='b'):
    lista = a+b+c

a = []
b = []
c = []


for i in range (7):

    a.append(lista[0])
    b.append(lista[1])
    c.append(lista[2])

    print (lista)
 

# for i in range(3):
#     lista1.append(i)
#     print (i)


# for i in range(4):
#     lista2.append(i)
#     print (i)


# lista3 = lista1 + lista2

# print (lista3)


















