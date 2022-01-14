import numpy as np

l = [1,2,3]
m = [1,2,3]


# Soma
print(l + m)

# Soma broadcasting
# print(l / 9)  # Dá erro, prof fez no colab e foi
# Não dá certo porque lista não é a mesma coisa que matriz dentro do numpy!! VER ARQUIVO C

# Quando o broadcasting não funciona
# np.array([1,2,3]) + np.array([1,2]) # ValueError: operands could not be broadcast together with shapes (3,) (2,)  --> dimensões inconsistentes dos arrays

# soma, subtração e divisão
print("combinação de operações: ",(l,m)/(l-2))