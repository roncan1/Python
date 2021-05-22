# 정수형
print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print(3*(3+1))

# --------------------------------------------
# 문자열
print('풍선')
print("나비")
print("가나다라마바사아")
print("9번 출력 "*9)

# --------------------------------------------
# boorean
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 < 10))

# --------------------------------------------
# 변수

# 변수 사용 x
# print("우리집 강아지의 이름은 연탄이예요")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일까요? True")

# 변수 사용 o
animal = "강아지"
name = "복실이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "예요")
print(animal + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

# --------------------------------------------
# 연산자
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

print(2**3)
print(5 % 3)
print(5//3)

print(10 > 3)
print(10 < 3)
print(4 >= 7)
print(5 <= 5)
print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)
print(4 != 2)
print(not(4 != 2))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

# --------------------------------------------
# 수식
print(2 + 3 * 4)
print((2 + 3) * 4)

number = 2 + 3 * 4
print(number)
number = number + 2
print(number)

number += 2
print(number)
number -= 2
print(number)
number *= 2
print(number)
number /= 2
print(number)

number %= 5
print(number)

# --------------------------------------------
# 숫자처리함수(메소드)
print(abs(-5))     # 절대값

print(pow(4, 2))   # 제곱

print(max(5, 12))  # 최대값
print(min(5, 12))  # 최소값

print(round(3.14)) # 반올림
print(round(5.99)) # 반올림

from math import * # math 안의 모든것을 이용
print(floor(4.99)) # 내림
print(ceil(3.14))  # 올림
print(sqrt(3.14))  # 제곱근

# --------------------------------------------
# 랜덤함수

from random import *      # random 안의 모든것을 이용
print(random())           # 0.0 ~ 1.0 미만의 임의의 값 생성 
#                           ex) 0.3652718665698862

print(random() * 10)      # 0.0 ~ 10.0 미만의 임의의 값 생성
#                           ex) 7.171213323553429

print(int(random() * 10)) # 0 ~ 10 '미만'의 임의의 값 생성
#                           ex) 8

print(int(random() * 10) + 1) # 1 ~ 10 '이하'의 임의의 값 생성
#                           ex) 8

# 로또
print(int(random() * 45) + 1) # 1 ~ 45 '이하'의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 '이하'의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 '이하'의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 '이하'의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 '이하'의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 '이하'의 임의의 값 생성

print(randrange(1, 46))  # 1 ~ 46 '미만'의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 '미만'의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 '미만'의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 '미만'의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 '미만'의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 '미만'의 임의의 값 생성