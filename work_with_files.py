import json

path = r'C:\Users\sveta\Downloads\csvjson.json'

def read_large_file(path):
    '''Функция для построчного чтения большого json-файла'''
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for line in data:
            yield line

        # content = file.read()
        # print(f"Содержимое в UTF-8: {content}")
        # content = json.load(file)
        # print(f'прочитано {len(content)} строк')

for item in read_large_file(path):
    print(item)
