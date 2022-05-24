# 1
# def f(x):
#     y = 10 * x
#     print("함수안 y = ", y)
#     return y

# print(f(10))
# y = 1000
# print(y)

#도전문제 1
# def diffsum():
#     a,b,c = map(int, input().split())
#     sum = a + b + c
#     diffsum = (a*a) + (b*b) + (c*c)
#     return abs(diffsum) - abs(sum)
    
# print(diffsum())

# 2
# z = 3
# def f2(x):
#     y = z * x
#     print("y =", y)
#     print("z =", z)
#     return y
# print(f2(10))

# 3
# z = 3
# def f3(x):
#     z = 99
#     y = z * x
#     print("y =", y)
#     print("z =", z)
#     return y
# print(f3(10))

# 4
# z = 3
# def f4(x):
#     global z
#     z = 99
#     y = z * x
#     print("y =", y)
#     print("z =", z)
#     return y
# print(f4(10))
# print(z)

# 도전문제 2
m = 0
def diffsum():
    global m
    a,b,c = map(int, input().split())
    sum = a + b + c
    diffsum = (a*a) + (b*b) + (c*c)
    result = abs(diffsum) - abs(sum)
    if m > result:
        m = result
    return result
    
print(diffsum())