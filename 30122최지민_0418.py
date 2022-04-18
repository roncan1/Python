# 1
# a = [1.3, 2.6, 3.5, 4.7, 5.2]
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)

# 2
# a = [1.3, 2.6, 3.5, 4.7, 5.2]
# a = list(map(int, a))
# print(a)

# 3
# a = list(map(str,range(10)))
# print(a)

# 4
# a = map(int, input().split())
# print(a)
# a = list(a)
# print(a)

# 5
# a = [10,4,67,53,6,3,9]
# print('리스트의 최소값은',min(a))
# print('리스트의 최댓값은',max(a))
# print('리스트 값들의 합은',sum(a))

# 도전문제 1
# data = map(int, input().split())
# listA = list(data)
# print('리스트의 최댓값은', max(listA))
# print('리스트 값들의 합은', sum(listA))

# 6
# list2d = [[10,20], [30,40], [50,60]]
# print(list2d)

# 7
# list2d = [[10,20], [30,40], [50,60]]
# print(list2d[0][0])
# print(list2d[1][1])
# print(list2d[2][1])
# list2d[1][0] = 88
# print(list2d)

# 8
# jaggedList = [[10,20,30],[40,50],[60,70,80,90]]
# print(jaggedList)

# 9
# jaggedList = [[10,20,30],[40,50],[60,70,80,90]]
# jaggedList[0].append(1111)
# print(jaggedList)

# jaggedList[0].append(2222)
# print(jaggedList)

# jaggedList[2].extend([3333,4444])
# print(jaggedList)

# 도전문제 2
# peopleList = [[],[],[],[],[]]
# for i in range(5):
#     tmp = list(map(str, input("입력하시오").split()))
#     peopleList[i].extend(tmp)
# print(peopleList)


# 10
# jaggedList = [[10,20,30],[40,50],[60,70,80,90]]
# for i in range(len(jaggedList)):
#     for j in range(len(jaggedList[i])):
#         print(jaggedList[i][j], end=' ')
#     print()

# 11
# array = [[0 for col in range(5)] for row in range(10)]
# print(array)
# array = [['*' for col in range(5)] for row in range(10)]
# print(array)

# 12
# array = [[0]*5 for i in range(10)]
# print(array)