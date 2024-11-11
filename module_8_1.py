def add_everything_up(a, b):
    try:
        return print(f'{a+b}')
    except TypeError:
        return print(f'{str(a)+str(b)}')

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)