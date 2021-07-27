# Algoritmo: Números Felizes
# Autor: Anderson da Silva Costa

n = int(input('Insira um número inteiro: '))

print(f'Números Felizes entre 1 e {n} são: ')
for num in range(1,n):
    feliz = num # Possível Número Feliz
    num = str(num)
    cont = 0
    while True:
        aux = 0
        if (num == '1'):
            print(feliz, '', end='') # Serve para exibir os valores lado a lado.
            break
        elif (cont >= 100):
            break
        else:
            cont = cont + 1
            for i in range(0,len(num)):
                aux = aux + (int(num[i]))**2
        num = str(aux)
