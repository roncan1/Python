# 문자열
sentence = '나는 소년입니다'
print(sentence)

sentence2 = '파이썬은 쉬워요'
print(sentence2)

sentence3 = """
나는소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

# --------------------------------------------
# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6전까지
print("뒷자리 : " + jumin[7:]) # 7부터 끝까지
print("뒷자리(역순) : " + jumin[-7:]) # 끝부터 7까지

# --------------------------------------------
# 문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # []자리가 대문자인지 아닌지
print(len(python))
print(python.replace("Python", "Java")) # Python을 Java로 바꿔 출력

index = python.index("n") # n이 몇번쨰에 있는지
print(index)
index = python.index("n", index + 1) # 2번쨰 n이 몇번쨰에 있는지
print(index)

print(python.find("Python"))

print(python.count("n"))

# --------------------------------------------
# 문자열포멧

# 방법 1 
print("나는 %d살입니다." % 18)
print("나는 %s을 좋아해요." % "파이썬")

# 방법 2
print("나는 {}입니다.".format(18))
print("나는 {}살인 {}입니다.".format(18, "최지민"))
print("나는 {1}살인 {0}입니다.".format(18, "최지민"))

# 방법 3
print("나는 {age}살인 {name}입니다.".format(age = 18, name = "최지민"))
print("나는 {age}살인 {name}입니다.".format(name = "최지민", age = 18))

# 방법 4
age = 18
name = "최지민"
print(f"나는 {age}살인 {name}입니다")

# --------------------------------------------
# 탈출문자

# 저는 "최지민"입니다.
print("저는 \"최지민\"입니다.")

# C:\Users\82102\Desktop\python
print("C:\\Users\\82102\\Desktop\\python")

# PineApple
print("Red Apple\rPine")

# RedApple
print("Redd\bApple")

# Red   Apple
print("Red\tApple")