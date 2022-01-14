import numpy as np

# Soma
l = [1,2,3]
m = [1,2,3]
x = np.add(l,m)
print("x:",x)
print("shape:",x.shape)

# Subtração
l = [1,2,3]
m = [1,2,3]
x = np.subtract(l,m)
print("x:",x)
print("shape:",x.shape)


# Multiplicação
l = [1,2,3]
m = [1,2,3]
x = np.multiply(l,m)
print("x:",x)
print("shape:",x.shape)

l = [1,2,3]
x = np.multiply(l,3)
print("x:",x)
print("shape:",x.shape)

# Divisão
l = [1,2,3]
m = [1,2,3]
x = np.divide(l,m)
print("x:",x)
print("shape:",x.shape)

# Soma 2D
l = [[1,2],[3,4]]
m = [[1,2],[3,4]]
x = np.add(l,m)
print("x:\n",x)
print("shape: ", x.shape)