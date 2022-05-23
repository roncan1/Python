def days1(month):
    if (month == 1,3,5,7,8,10,12):
        return 31
    elif (month == 2):
        return 28
    elif (month == 4,6,9,11):
        return 30
    
def add(x,y):
    return x + y

def sum(a,b,c):
    s = a + b + c
    return s

def monthCheck(year, month):
    if (month == 1,3,5,7,8,10,12):
        return 31
    elif (month == 2):
        if (year%4 == 0) & (year%100 != 0) | (year%400 == 0):
            return 29
        else :
            return 28
    elif (month == 4,6,9,11):
        return 30