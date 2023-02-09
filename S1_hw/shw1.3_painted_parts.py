# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

# Решение:
# Вероятность благоприятных событий m = 3 из 9
# Общее число событий n = 3 из 15

import math
m = math.factorial(9) / (math.factorial(3) * math.factorial(6))
n = math.factorial(15) / (math.factorial(3) * math.factorial(12))

prob = round(m/n * 100, 2)

print(m)
print(n)
print(prob,'%')