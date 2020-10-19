'''
exc 2
Preencher uma lista de 8 elementos inteiros. 
Mostrar o vetor e informar quantos números são maiores que 30.
Somar todos os números.
'''
#Resolução do exerc 2 por BOT-Samuel

lista2 = []
n = 0

for i in range(8):
    x = int(input("Digite os valores inteiros:"))
    lista2.append(x)

lista2.sort()
print(lista2[:])

for c in range(8):
    if (lista2[c]>30):
        n = n + 1
print ("Há {0} números maiores que 30.".format(n))
