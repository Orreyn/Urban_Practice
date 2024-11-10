import io

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a+', encoding='utf-8')
    for i in range(0, len(strings)):
        file.write(strings[i])
        file.write('\n')
    file = open(file_name, 'r', encoding='utf-8')
    line_num = 1
    x = 0
    for line in file.readlines():
        if line == '':
            break
        print(file.seek(x)) # Я понятия не имею почему, но оно работало ТОЛЬКО через print, без него tell выдавал только последнюю цифру
        x += len(line)
        temp_dict = {f'{line_num}, {file.tell()}': line}
        strings_positions.update(temp_dict)
        line_num += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)