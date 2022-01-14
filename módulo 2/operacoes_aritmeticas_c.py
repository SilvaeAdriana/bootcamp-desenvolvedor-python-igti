import numpy as np
x = np.ones((2,2))
y = np.eye(2)


print(x+8)
print(x*8)  # Broadcasting

# Multiplicação 
print(" Multiplicação de dois arrays:\n", x * y)
print(" Multiplicação com float/int:\n", x * 2)  # broadcasting


# Multiplicação matricial: 3 maneiras de ser realizado o mesmo procedimento, multiplicando matrizes x e y
print(" Multiplicação matricial (np.dot):\n", np.dot(x,y))
print(" Multiplicação matricial (0):\n", x @ y)
print(" Multiplicação matricial (.dot):\n", x.dot(y))

print(10 * np.ones((10,10)))


''' 
Exemplo de aplicação:
Solução de um sistema de equações:
    a + 2*b = 7
    3 * a - 2 * b = -11
    solução analítica: [a,b] = (-1,4)
    Matricialmente, este problema tem a seguinte forma:
    Ax = c, onde:
    X = [a,b]
    A = [[1,2],[3,-2]]
    C = [7,-11]
    solução numérica: x = inv(A) @ c
'''

# Definição do problema do comentário acima
A = np.array([[1,2],[3,-2]])
C = np.array([[7],[-11]])
print("A:\n", A)
print("C:\n", C)


# Solução
# Linalg pacote de álgebra linear
x = np.dot(np.linalg.inv(A),C)
# x = np.linalg.inv(A) @ C
print("(a,b):", x.ravel())