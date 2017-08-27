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
print (A)
