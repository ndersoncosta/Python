# Algoritmo: Números Educados (Retorna os que não são educados)
# Autor: Anderson da Silva Costa

# Obs! Os únicos números não educados são as potências de dois! E isto se
# confirmou nos resultados!

n = int(input('Insira um número inteiro: '))

print(f'Números não Educados entre 1 e {n} são:')

#print(f'Números Educados entre 1 e {n} são:')
#print('1 2','', end='')
 
for num in range(3,n+1):
    # educ = num
    not_educ = num
    for i in range(1,int(num/2)+2):
        soma = 0
        for j in range(i,int(num/2)+2):
            if (soma < num):
                soma = soma + j
        if (soma == num):
            #print(educ, '', end='')
            break
        
    # Esperando Vetores
    if (i == int(num/2)+1):
        print(not_educ, '', end='')
                
