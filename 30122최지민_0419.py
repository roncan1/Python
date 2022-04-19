# 1
# array = [[0 for col in range(5)] for row in range(10)]
# print(array)
# array = [['*' for col in range(5)] for row in range(10)]
# print(array)

# 2
# array = [[0]*5 for i in range(10)]
# print(array)

# 3
# array = [[0]*11 ]*10
# print(array)
# array[3][1] = "@"

# 4
# print("내 이름은 %s입니다." % '홍길동')
# print("나는 %d살 입니다" %12)
# print("원주율의 값은 %f입니다." % 3.14)
# print("%d 곱하기 %d는 %d이다" % (2,3,6))
# print("%s의 %s과목 점수는 %d점이다" % ('a', 'b', 123))

# 도전문제
# name = "tom"
# age = 13
# print("%s is %d years old" % (name, age))

# a = 10
# b = 3
# print("%d / %d = %.3f" % (a,b,a/b))

# 5
# print("내 이름은 {}입니다.".format("홍길동"))
# print("{2} {1} {0} {2} {0}".format(0,10,30))

# 6
# month = 1
# while month <=12:
#     print(f'2020년 {month}월')
#     month+=1
    
# 도전문제 2
a = 3
b = 12
print("{:5}".format(a))
print("x{:4}".format(b))
print("-----")
print("{:5}".format(a*b))

a = "123456"
b = "7890"
a = int(a)
b = int(b)
print("{:10,}".format(a))
print("+{:9,}".format(b))
print("----------")
print("{:10,}".format(a+b))