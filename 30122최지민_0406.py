# 시퀸스 객체와 난수
# 1
# import random
# city = ['서울','대전','인천','대구','부산','광주','목포',]
# i = 0
# while i < 4:
#     print(random.choice(city))
#     i+=1
    
# 도전문제 1
# import random
# number = list(range(1, 46))
# myList = []
# while len(myList) < 6:
#     num = random.choice(number)
#     if num not in myList:
#         myList.append(num)
# print(myList)

# import random
# myList = []
# while len(myList) < 6:
#     num = random.randint(1, 45)
#     if num not in myList:
#         myList.append(num)
# print(myList)

# import random
# numbers = list(range(1, 46))
# random.shuffle(numbers)
# print(numbers[0:6 ])

# import random
# numbers = list(range(1, 46))
# random.shuffle(numbers)
# numbers.sort()
# print(numbers[0:6 ])

# 2 
i = j = 0
while i < 5:
    print(i, end=' ')
    i+=1
print('')
while j < 5:
    if j== 3:
        break;
    print(j, end=' ')
    j+=1