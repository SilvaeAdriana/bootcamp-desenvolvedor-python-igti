import numpy as np

x = np.array([[1,3,7],[4,11,21],[42,8,9]])
print("x:\n", x)

# Reshape: transformar a matriz em um vetor coluna
# (3,3) vira (9,1): 3*3 = 9*1 = 9
print("transformação em um vetor em coluna: \n", x.reshape(9,1))

'''
imprime:
transformação em um vetor em coluna:
 [[ 1]
 [ 3]
 [ 7]
 [ 4]
 [11]
 [21]
 [42]
 [ 8]
 [ 9]]
'''

# transposição de matriz
print(" x.transposta: \n", x.T)

'''
imprime:
 x.transposta:
 [[ 1  4 42]
 [ 3 11  8]
 [ 7 21  9]]
'''

# np.sum: soma em um dado eixo, axis ={0:linha, 1:coluna}
print(" x:\n",x)
print("soma de todos elementos de x: ", np.sum(x))
print(" soma de  ao longo das linhas: ", np.sum(x,axis=0)) # apresenta as soma em ordem do indice das linhas
print("soma de x ao longo das colunas: ",np.sum(x,axis=1))

'''
imprime:
 x:
 [[ 1  3  7]
 [ 4 11 21]
 [42  8  9]]
soma de todos elementos de x:  106
 soma de  ao longo das linhas:  [47 22 37]
soma de x ao longo das colunas:  [11 36 59]

'''

# np.mean: média em um dado eixo, axis ={0:linha, 1:coluna}
print(" x:\n",x)
print("média de todos elementos de x: ", np.mean(x))
print(" média de  longo das linhas: ", np.mean(x,axis=0)) # apresenta as médias em ordem do indice das linhas  (acho que está o contrário devido aos valores que imprime...)
print("média de x ao longo das colunas: ",np.mean(x,axis=1))

'''
imprime:
 x:
 [[ 1  3  7]
 [ 4 11 21]
 [42  8  9]]
média de todos elementos de x:  11.777777777777779
 média de  ao longo das linhas:  [15.66666667  7.33333333 12.33333333]
média de x ao longo das colunas:  [ 3.66666667 12.         19.66666667]

'''

# np.where, indenficação dos índices onde uma dada condição é
# atendida. Uso conjunto com indexação booleana
condicao = x % 2 == 0 # números pares
print("condição:\n", condicao)
i,j = np.where(condicao) # índices x[i,j] = x[condicao]
print("índice i (linhas): ", i)
print("índice j (colunas): ", j)

'''
imprime:
condição:
 [[False False False]
 [ True False False]
 [ True  True False]]
índice i (linhas):  [1 2 2]
índice j (colunas):  [0 0 1]
'''

# indexação booleana e slicing: selecionar as linhas
# de x que possuem algum número par
print("x:\n", x)
condicao = x % 2 == 0 # números pares
print("condicao: \n", condicao)

'''
imprime:
condicao:
 [[False False False]
 [ True False False]
 [ True  True False]]
'''

# se houver alguma condição True na linha, a soma será > 0
i_row = np.where(np.sum(condicao,axis=1))[0]
print("índice das linhas que possuem números pares: ", i_row)
print("linhas que possuem números pares: \n", x[i_row,:])

'''
imprime:
condicao:
 [[False False False]
 [ True False False]
 [ True  True False]]
'''