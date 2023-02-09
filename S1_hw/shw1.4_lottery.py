# В лотерее 100 билетов. 
# Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

# Решение:
# m = 2 из 2
# n = 2 из 100

# prob = (2/100)
# print(prob,'%')

import math
m = math.factorial(2) / (math.factorial(2) * math.factorial(0))
n = math.factorial(100) / (math.factorial(2) * math.factorial(98))

prob = round(m/n*100, 2)

print(m)
print(n)
print (prob,'%')