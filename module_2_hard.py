import random
def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password
n = random.choice(range(3, 20))
print('Рандомное число:', n)
result = get_password(n)
print('Для этого рандомного числа паролем является:', result)