porridge = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
N = int(input())
for i in range(N):
    ind = i % len(porridge)
    print(porridge[ind])
