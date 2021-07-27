# Implementação do Algoritmo de Ordenação HeapSort

# heapify: Construção da Heap
# Input: array (lista de valores)
#        n (tamanho do array)
#        i (nó atual)

from numpy import random as rd

def heapify(array, n, i):

	largest = i # Raiz da árvore como sendo o maior valor (inicialmente o primeiro valor da lista de entrada)
	left = 2*i + 1 # Nó Filho da esquerda
	right = 2*i + 2 # Nó Filho da direita

	# Se o Nó Filho da esquerda é maior que a Raiz Pai
	if (left < n and array[left] > array[largest]):
		largest = left

	# Se o Nó Filho da direita é maior que a Raiz Pai
	if (right < n and array[right] > array[largest]):
		largest = right

	# Se a Raiz Pai foi alterada
	if (largest != i):

		# swap do C++
		array[i], array[largest] = array[largest], array[i]

		# Heapify para a nova raiz
		heapify(array, n, largest)

def heapSort(array):
	# Comprimento do array
	n = len(array)

	# Construção da Heap
	for i in range(n, -1, -1):
		heapify(array, n, i)

	# Extrair elemento por elemento da heap
	# Obs! É n-1 pois o python é zero based e termina no elemento 1 pois o último não precisa remover
	for i in range(n-1, 0, -1):

		# swap do C++
		array[i],array[0] = array[0],array[i]
		heapify(array, i, 0)


def main():
	# Vetor Aleatório
	array = []
	for i in range(0,15):
		array.append(rd.randint(0,100))
	
	print(array)
	print('')

	heapSort(array)
	print(array)


if __name__ == '__main__':
	main()
