import collections

contador = collections.Counter()
contador['PR'] += 1000
contador['RJ'] += 10000
contador['PR'] += 500
print(contador)
