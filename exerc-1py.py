"""Exercício 1: faça um programa que solicite ao usuário números e os armazene
em um vetor de 30 posições. Crie uma função que recebe o vetor preenchido e
substitua todas as ocorrência de valores positivos por 1 e todos os valores
negativos por 0.


def substitui(vet):
    for i in range(30):
         if vet[i] >= 0:
            vet[i] = 1
         else:
            vet[i] = 0
    return vet
 
vet = [0]*30
for i in range(30):
    vet[i] = int(input('Digite um valor: '))
print (vet)
substitui (vet)
print (vet)"""

"""Exc2
def substitui(vet, tam):
    for i in range(tam):
        if vet[i] <= 0:

            vet[i] = 0
        elif vet[i] < 10:
            vet[i] = 1
        else:
            A
            [i] = 2
    return vet
 
tam = 20
 
A = [0]*tam
for i in range(tam):
    A[i] = int(input('Digite um valor: '))
substitui(A,tam)
print (A)"""


'''n1 = int(input("Digite um valor: "))
if n1 < 0:
    print (n1 * -1)
elif n1 > 10:
    n2 = int(input("Digite outro valor: "))
    print (n1 - n2)
else:
    print (n1/5.0)'''


arquivo = open('musica.txt', 'r')































































