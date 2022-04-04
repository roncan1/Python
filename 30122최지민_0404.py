# if문

# # 1
# a = int(input("숫자를 입력해주세요 : "))
# if a == 1:
#     print('와우!!')
#     print('1을 입력하셨습니다.')
# print('프로그램을 마칩니다.')


# # 도전문제
# a = int(input())
# b = int(input())

# if a+b > 100:
#     print('100 이상입니다.')
    

# # 2
# a = int(input("숫자를 입력해주세요 :"))
# if a == 1:
#     pass
# print('프로그램을 마칩니다.')

# # 3
# a = int(input("숫자를 입력해주세요 :"))
# if a >= 10:
#     print('와우! 10 이상이군요.')
#     if a % 2 == 0:
#         print('오오~ 작수를 입력하셨네요')
#     print('짝수 판별이 끝났습니다.')
# print('프로그램을 마칩니다.')

# # 4
# a = int(input("숫자를 입력해주세요 :"))
# if a % 2 == 0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')
# print('프로그램 종료')

# # 5
# if 0:
#     print('숫자 0')
# if 1:
#     print('숫자 1')
# if 100:
#     print('숫자 100')
# if -14:
#     print('숫자 -14.7')

# # 5
# if '':
#     print('빈문자')
# if ' ':
#     print('공백문자 1개')
# if 'Hello':
#     print('Hello?')
    
# # 6
# a = {}
# b = []
# if a:
#     print('빈 딕셔너리')
# if b:
#     print('빈 리스트')
# b = [1,2,3,4,5]
# if b:
#     print('요소가 있는 리스트')

# # 7
# birth = int(input('생일을 입력하세요 :'))
# if birth == 13 or birth == 3 :
#     print('생일이 3일 또는 13일 이시군요. 쿠폰 당첨!!')
# else:
#     print('쿠폰 증정 대상이 아닙니다.')
    
# # 8
# birth = int(input('생일을 입력하세요 :'))
# if 3 <= birth <= 13 :
#     print('생일이 3일에서 13일 사이네요. 쿠폰 당첨!!')
# else:  
#     print('쿠폰 증정 대상이 아닙니다.')
    
# # 9
# pt = int(input("점수를 입력하세요 :"))
# if pt >= 90:
#     print('A')
# elif 90 > pt >= 80:
#     print('B')
# elif 80 > pt >= 70:
#     print('C')
# elif 70 > pt >= 60:
#     print('D')
# else:
#     print('E')
    
# # 10

# food = input('음식 이름 :')
# if food == '피자':
#     print('16,000원')
# elif food == '햄버거':
#     print('사딸라!!')
# elif food == '김밥':
#     print('2,500원')
# else:
#     print('입력하신 음식이 메뉴에 없습니다.')
    
# 도전문제1
# year = input()

# yeara = year[0:4];
# print(yeara + "년")
# month = year[4:6];
# print(month + "월")
# day = year[6:8];
# print(day + "일")

# 도전문제2
# people = int(input())

# if people < 10:
#     print('단체할인 미적용 ' + str(people*50000) + '원 입니다.')
# else:
#     print('단체할인 적용 ' + str(people*10000) + '원 입니다.')
    
    
# 반복문

# 1
# for i in range(5):
#     print('안녕하세요?')
    
# 2
# for i in range(5):
#     print('안녕하세요?',i)
    
# 3
# for i in range(1, 13):
#     print(i, '월', end=': ')
    
# 4
# for i in range(1, 10, 2):
#     print(i, end=' ')
    
# 5
# for i in range(10,0,-1):
#     print(i, end=' ')

# 6
# for i in range(5):
#     print(i, end=' ')
# print('')
# for i in reversed(range(5)):
#     print(i, end=' ')    

# 도전문제 1
# from tracemalloc import start


# b = 0;
# for i in range(5):
#     a = int(input())
#     if a > b:
#         b = a
# print(b)

# # 7
# loop = int(input('1 부터 얼마까지 출력할까요?'))
# for i in range(1, loop +1):
#     print(i, end=' ')

# # 8
# start = int(input('시작값 :'))
# stop = int(input('끝값 :'))
# hop = int(input('증가값 :'))

# for i in range(start, stop+1, hop):
#     print(i, end=' ')
    
# 9
# tupleA = ('서울','인천','수원','성남','일산')
# for i in tupleA:
#     print(i, end='/')
# print('')
# for i in reversed(tupleA):
#     print(i, end='/')

# 10
# str = 'Hello Python'
# for i in str:
#     print(i, end='/')

# 도전문제 2
# girlfriend = ('소원','예린','은하','유주','신비','엄지')
# name = input()
# count = 0;
# flag = False
# for i in girlfriend:
#     count += 1
#     if i == a:
#         print(count)
#         flag = True
# if flag == False:
#     print('리스트에 없는 이름입니다.')
    
# while문
# 1
# i = 1
# while i < 11:
#     print(i, end='/')
#     i+=1
    
# 도전문제 1
# i = 1
# while i <= 100:
#     if i%4 == 0:
#         print(i)
#     i += 1
        
# 도전문제 2
import random
i = 1; j = 2
count = 0
while(i!=j):
    i = random.randint(1,6)
    j = random.randint(1,6)
    print(i,j)
    count += 1
print('두 주사위의 값이 같습니다. 총 ', count, '번 반복했습니다.')
