#           단순출력
#1
print("Experience is the best teacher");print('No news is good news.')

#2
print('I need more margin');
print('And I also 시공조아');

#2
print('안녕하세요?')
print('반갑습니다.') #인사말을 출력합니다.

#3
print('안녕하세요?')
"""
주석 처리
"""
print('반갑습니다.')

#4
# b = 100
# if(b >= 10) {
#     print("a는 10보다 크다.")
#     b = 0;
# }
# print("프로그램을 종료합니다.")

#4
a = 100
if(a >= 10) :
    print("a는 10보다 크다.")
    a = 0;
print("프로그램을 종료합니다.")

#           연산자, 변수
#1
print(1+1)
print(4-2)
print(3*4)
print(10/2)

#2
print(28/8)

#3 
# //는 소수점 이하 버리기
a = (28//8)
print(a)
print(type(a))

#4
import sys
t1 = sys.maxsize
t2 = sys.maxsize +1
print(t1)
print(t2)
print(type(t1))
print(type(t2))
print(t1 * t1)

#5
# **는 제곱
print(5%2)
print(33%5)
print(2**10)

#6
print(5%2.2)
print(5%2.0)

#7
print(int(5.3))
print(int(7.7))
print(int('710325'))

#8
print(3.5 + 2.1)
print(4.3 - 2.7)
print(1.5 * 3.1)
print(5.5 / 3.1)

#9
print(0.2 +0.1)

#10
print(6 + 6.2)

#11
print(float(7))
print(float(2*4))
print(float('13.445'))

#12
print(3 + 7 * 4)
print ((3 + 7) * 4)

#13
a = 7
print(a)
a = 10
print(a)

#14
b =10
c = 10.7
d = '10.338'

print(type(b))
print(type(c))
print(type(d))

#15
e, f, g = 10, 20, 30
h = i = j = 40
print(e, f, g)
print(h, i, j)

#16
k = None
print(k)
k = 10
print(k)

#17
m = 100
m = m + 1
print(m)
m += 1
print(m)

#18
a = input()
print('[',a,']')

#19
a = input("인사말을 입력하세요")
print(a)

#20
b = input("첫 번째 정수를 입력해주세요 :")
c = input("두 번째 정수를 입력해주세요 :")
print(b + c)
print(int(b) + int(c))

#21
b = int(input("첫 번째 정수를 입력해주세요 :"))
c = int(input("두 번째 정수를 입력해주세요 :"))
print(b + c)

#22
a, b = input('학교명과 성명을 입력하세요 :').split()
print('학교명:',a)
print('성명:',b)

#23
a, b = input('주민번호 13자리를 입력해주세요:').split('-')
print(a)
print(b)

#24
a,b = input('정수 2개를 입력하세요 :').split()
print(a+b)

#25
a,b = input('정수 2개를 입력하세요 :').split()
a = int(a)
b = int(b)
print(a+b)

#26
a,b = map(int, input('정수 2개를 입력하세요 :').split())
print(a+b)

#27
print(100)
print('안녕하세요')
print(10, 20, 30)
print('Hello', 'World')

#28
print(10, 20, 30, sep=',')
print(10, 20, 30, sep=' => ')
print(10, 20, 30, sep='')

#29
print('인생은 짧다.\n내 다리도 짧다.')

#30
print('인생은 짧다.')
print('내 다리도 짧다.')
print('------------')
print('인생은 짧다. ',end='')
print('내 다리도 짧다')

#31
print('저 산 위에 바위는 크다')

