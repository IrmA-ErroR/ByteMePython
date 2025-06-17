import csv
from datetime import datetime
from collections import defaultdict

class CoffeeAnalysis:
    def __init__(self):
        self.coffee_stats = defaultdict(int)
        self.hourly_stats = defaultdict(int)
        self.cash_type_stats = defaultdict(int)
        self.total_income = 0.0

    def update(self, cup):
        self.coffee_stats[cup['coffee_name']] += 1
        hour = cup['datetime'].hour
        self.hourly_stats[hour] += 1
        self.cash_type_stats[cup['cash_type']] += 1
        self.total_income += cup['money']

    def create_report(self):
        print('\n\tОтчет')
        print(f"\nОбщая выручка: {self.total_income:.2f}$")
        print('Продано:')
        for coffee, value in sorted(self.coffee_stats.items()):
            print(f'\t{coffee} - {value}')
        print('Количество проданных чашек по часам:')
        for hour, value in sorted(self.hourly_stats.items()):
            print(f'{hour} - {value}')


def read_coffee_csv(my_path):
    '''Генератор для чтения данных о продажах кофейных автоматов. Чтение построчное, с преобразованием типов и проверкой. Создает словари с очищенными и преобразованными полями данных.'''

    with open(my_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                processed = {
                    'date' : row['date'],
                    'datetime' : datetime.strptime(row['datetime'], '%Y-%m-%d %H:%M:%S.%f'),
                    'cash_type' : row['cash_type'].strip().lower(),
                    'card' : row['card'].strip().upper(),
                    'money' : float(row['money']),
                    'coffee_name' : row['coffee_name']
                }
                yield processed

            except (ValueError, KeyError) as e:
                print(f"\nSkipping malformed row: {row}. Error: {str(e)}")
                continue


analysis = CoffeeAnalysis()
my_path = r'C:\Users\sveta\OneDrive\Документы\ByteMePython\data\coffee_data_index_1.csv'
for cup in read_coffee_csv(my_path):
    # print(f"{cup['datetime']} - {cup['coffee_name']} - {cup['money']}$")
    analysis.update(cup)

analysis.create_report()
