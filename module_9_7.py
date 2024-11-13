def is_prime(func):
    def wrapper(*args):
        i = func(*args)
        prime = True
        if i <= 1:
            print('Числа меньше 2 ни простые, ни составные')
        elif i == 2 or i == 3:
            prime = True
            print('Простое')
        elif i % 2 == 0:
            prime = False
            print('Составное')
        else:
            a = int(i ** 0.5)
            if a == 2:
                prime = True
                print('Простое')
            else:
                for j in range(3, a + 1, 2):
                    if i % j == 0:
                        prime = False
                        print('Составное')
                        break
                    else:
                        prime = True
                if prime is True:
                    print('Простое')
        return i
    return wrapper


@is_prime
def sum_three(*args):
    summa = 0
    for i in args:
        summa += i
    return summa


result = sum_three(2, 3, 6)
print(result)