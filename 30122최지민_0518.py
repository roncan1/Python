def twoTimes(x):
    y = 2 * x
    return y

a = twoTimes(2)
b = twoTimes(10)
print(a)
print(b)

def function1(value):
    if (value%2 == 0):
        return "짝수"
    else :
        return "홀수"
    
def function2(year):
    if (year%4 == 0) & (year%100 != 0) | (year%400 == 0):
        return "윤년"
    else :
        return "평년"
    
def days1(month):
    if (month == 1,3,5,7,8,10,12):
        return 31
    elif (month == 2):
        return 28
    elif (month == 4,6,9,11):
        return 30
    
print(days1(2))