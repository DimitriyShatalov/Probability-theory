# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 

# Решение:
# Вероятность благоприятных событий m = 4 из 13
# Общее число событий n = 4 из 52

import math
m = math.factorial(13) / (math.factorial(4) * math.factorial(9))
n = math.factorial(52) / (math.factorial(4) * math.factorial(48))

prob = round(m/n*100, 2)

print(m)
print(n)
print (prob,'%')

