# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# Решение:

import math
m = (math.factorial(48) / (math.factorial(4) * math.factorial(44))) * \
    (math.factorial(4) / (math.factorial(0) * math.factorial(4)))
n = math.factorial(52) / (math.factorial(4) * math.factorial(48))

prob = round((1 - m/n)*100, 2)

print(m)
print(n)
print(prob,'%')
