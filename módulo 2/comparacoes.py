import numpy as np
# Indexação booleana: filtragem nos arrays
# Comparações

# comparações booleanas
A = np.array([1,2,3])
B = np.array([2,0,2])
s = 3

# Menor
print("Comparação menor: ")
# compara elemento a elemento
print(A<B)
print(A<s)

# Maior
print("Comparação maior: ")
# compara elemento a elemento
print(A>B)
print(A>s)

# Igualdade
print("Comparação igualdade: ")
# compara elemento a elemento
print(A == B)
print(A == s)

# Indexação booleana: um novo subarray contendo uma
# cópia dos elementos em que a condição de verificação se aplica
# OPERAÇÃO DE FILTRO: retorna valores que são verdadeiros conforme condição dada
cond = A <= 2
D = A[cond]
print("A:", A) # array dado
print("condição: ", cond)
print("D:", D) # valores que correspondem a condição dentro do array 
