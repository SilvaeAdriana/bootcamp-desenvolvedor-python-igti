# O set nõ admite repetidos
sett = {1,2,3,3,4}
sett1 = {1,2,3}
sett2 = {3,4}
# Imprime: {1, 2, 3, 4}
print(sett)
print(1 in sett)
# sett.append(6): não acata append
# Para adicionar elemento, usa-se add
sett.add(6)
print(sett)

# Somando sets
sett1.update(sett2)
print(sett1)