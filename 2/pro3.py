import random

correctCnt, wrongCnt=0, 0

for i in range(1, 11):
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    answer = int(input(f'{i}번>> {x}+{y} = '))

    if answer == x+y:
        print("정답입니다.")
        correctCnt += 1
