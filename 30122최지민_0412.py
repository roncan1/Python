#도전문제 1
# a = input()
# b = input()
# while a != b:
#     a = input()
#     b = input()
#     if a == b:
#         break
    
# 1
# student = ['이명우', '김진호', '윤찬진', '김호연', '나찬수', '김민환']
# for a in student:
#     if a[0]== '김':
#         continue
#     print(a)

# 2
# for i in range(3):
#     print('i의 값 :',i)
#     for j in range(4):
#         print(' - j의 값 :',j)
#     print('안쪽 반복문의 실행이 종료되었음')
# print('바깥쪽 반복문의 실행이 종료되었음')

# 3
# for a in range(5):
#     print('*', end='')
    
    
# 4
# for b in range(6):
#     for a in range(5):
#         print('*',end='')


# 5
# for b in range(6):
#     for a in range(5):
#         print('*',end='')
#     print('')

# 도전문제 2
# for b in range(5):
#     for a in range(7):
#         if a == 6:
#             print('K',end='')
#         elif a == 0:
#             print('K',end='')
#         else:
#             print('A',end='')
#     print('')
    
# 도전문제 3
# for b in range(5):
#     for a in range(7):
#         if b%2 == 0:
#             print('K',end='')
#         else:
#             print('A',end='')
#     print('')

# 도전문제 4
# a = 1
# while a < 7:
#     for b in range(a):
#         print('A', end='')
#     print('')
#     a += 1

# 리스트와 튜플 응용
# 1
# a = [1,2,3,4,5]
# print(a)
# a.append(10)
# print(a)
# a.append(6)
# print(a)

# 2
# b = []
# print(b)
# for i in range(5):
#     temp = input('리스트에 추가할 값을 입력하세요:')
#     b.append(temp)
# print(b)

# 3
# a = [1,2,3,4,5]
# print(a)
# a.append([6,7,8])
# print(a)
# print(a[5])

# 4
# b = [1,2,3,4,5]
# print(b)
# b.extend([6,7,8])
# print(b)

# 5
# c = [1,3,4,5,7]
# print(c)
# c.insert(1,2)
# print(c)
# c.insert(5,6)
# print(c)
# c.insert(7,8)
# print(c)

# 6
# d1 = [1,2,7,8]
# d2 = [1,2,7,8]
# d1.insert(2,[3,4,5,6])
# print(d1)
# d2[2:2] = [3,4,5,6]
# print(d2)

# 도전문제 1
# a = [1,3,5,7,10]
# a.append(11)
# a.insert(3,6)
# a[5:5] = [8,9]
# print(a)

# 7
# a = [1,2,3,4,5]
# a.pop()
# print(a)
# a.pop()
# print(a)

# 8
# b = [1,2,3,4,5]
# b.pop(2)
# print(b)
# del b[1]
# print(b)

# 9
# c = [1,3,5,7,9]
# c.remove(6)
# print(c)

# 10
# d = [1,3,5,7,9,11]
# for i in range(2):
#     data = int(input("리스트에서 삭제할 값을 입력하세요 :"))
#     if data in d:
#         d.remove(data)
#         print(d)
#     else:
#         print('리스트에 존재하지 않는 값입니다.')
#         print(d)

# 11
# a = [10,20,30,40,50]
# print(a.index(40))
# print(a.index(25))

# 도전문제 2
# lista = [1,2,3,4,5,6,7,8]
# data = int(input())
# if data in lista:
#     print(lista.index(data))
# else:
#     print('값이 리스트에 없습니다.')
    
# 12
# a = [10,20,30,40,50,60,40]
# print(a.index(40))

# 13
# a = [10,20,30,40,50,60,40]
# print(a.count(40))

# 14
# b = [30,10,40,20,60,50]
# b.sort
# print(b)
# b.sort(reverse=True)
# print(b)

# 15
# b = [30,10,40,20,60,50]
# print(b)
# b.reverse()
# print(b)

# 도전문제 3
test = [3,6,2,1,7,8,9,3,2,6,7,5,2]
data = int(input())
if data in test:
    if test.count(data) > 1:
        print(test.count(data))
    else:
        print(test.index(data),'개')
else:
    print('값이 리스트에 없습니다.')