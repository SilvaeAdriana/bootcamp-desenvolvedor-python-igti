import numpy as np

# Criando array
x = np.array([[1,2],[3,4]])
y = np.array([1,5,3.5])
print("x: \n", x)
print("y: \n", y)


# Comparações ponto a ponto
print(" Comparação com um array escalar (>): \n", x > 2)
print(" Comparação com um array escalar (>=): \n", x >= 2)
print(" Comparação com um array escalar (<): \n", x < 2)
print(" Comparação com um array escalar (<=): \n", x <= 2)
# print("Comparação entre arrays (==): \n",x ==x)
# print("Comparação entre arrays (>): \n",x > x)
# print("Comparação entre arrays (<): \n",x < x) # broadcasting


# INDEXAÇÃO BOOLEANA
x = np.array([[1,3,7],[4,11,21],[42,8,9]])
print("x:\n", x)

# indexação booleana: retornar o número de elementos
# Maiores que k
k = 10
condicao = x > k
print(" condição: \n", condicao)
print(f"elementos maiores que {k}:", x[condicao])
print(f" número de elementos maiores que {k}:", len(x[condicao]))


# indexação booleana: extração dos números pares
condicao = x% 2 == 0 # números pares
print("condicao: \n", condicao) # retorna valores booleanos das comparações
print("números pares: ", x [condicao])

# indexação booleana: extração dos números ímpares
condicao = x% 2 == 1 # números ímpares
print("condicao: \n", condicao) # retorna valores booleanos das comparações
print("números pares: ", x [condicao])
