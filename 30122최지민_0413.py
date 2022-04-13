# 1
# a = [10,20,30,40,50,60,40]
# print(a.index(40))

# 2
# a = [10,20,30,40,50,60,40]
# print(a.count(40))

# 3
# b = [30,10,40,20,60,50]
# b.sort
# print(b)
# b.sort(reverse=True)
# print(b)

# 4
# b = [30,10,40,20,60,50]
# print(b)
# b.reverse()
# print(b)

# 도전문제 1
# test = [3,6,2,1,7,8,9,3,2,6,7,5,2]
# data = int(input())
# if data in test:
#     if test.count(data) > 1:
#         print(test.count(data),'개')
#     else:
#         print(test.index(data))
# else:
#     print('값이 존재하지 않습니다.')                                                                                                                     
    
# 5
# a = [1,2,3,4,5]
# b = a
# print(id(a))
# print(id(b))
# print(a)
# print(b)

# 6
# a = [1,2,3,4,5]
# b = a.copy()
# print(a)
# print(b)
# b[3] = 400
# print(a)
# print(b)

# 7
# c = [1,2,3,4,5]
# d = [6,7,8,9,10]
# c.clear()
# del d[:]
# print(c)
# print(d)

# 8 
# a = ['서울','인천','대전','춘천','전주','광주','부산','울산']
# for i in a:
#     print(i, end='-')

# 9
# a = ['서울','인천','대전','춘천','전주','광주','부산','울산']
# for index, city in enumerate(a) :
#     print(city, '(', index, ')')

# 10
# a = [i for i in range(10)]
# print(a)

# 11
# b = [i+1 for i in range(10)]
# print(b)

# 12
# listA = [i+5 for i in range(10) if i%2 == 1]
# print(listA)

# 13
# a = [1.3, 2.6, 3.5, 4.7, 5.2]
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)

# 14
# a = [1.3, 2.6, 3.5, 4.7, 5.2]
# a = list(map(int, a))
# print(a)

# 15
# a = list(map(str,range(10)))
# print(a)

# 16
# a = map(int, input().split())
# print(a)
# a = list(a)
# print(a)

# 17
# a = [10,4,67,53,6,3,9]
# print('리스트의 최소값은',min(a))
# print('리스트의 최댓값은',max(a))
# print('리스트 값들의 합은',sum(a))

# 도전문제 2
# data = map(int, input().split())
# listA = list(data)
# print('리스트의 최댓값은', max(listA))
# print('리스트 값들의 합은', sum(listA))



 