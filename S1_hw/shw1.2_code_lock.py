# На входной двери подъезда установлен кодовый замок, 
# содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

# Решение:
# m = 3 из 3
# n = 3 из 10

import math
m = math.factorial(3) / (math.factorial(3) * math.factorial(0))
n = math.factorial(10) / (math.factorial(3) * math.factorial(7))

prob = round(m/n * 100, 2)


print(m)
print(n)
print(prob,'%')