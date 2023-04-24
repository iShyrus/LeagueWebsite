import math 

def area_of_equilateral(num):

    area = (num*num*math.sqrt(3))/4
    return(area)





def count_fred_and_ted(list):
    count =0
    for i in list:
        name =i
        if(name =="fred" or name =="ted"):
            count+=1
    return(count)



def sum_of_greatest_two(a,b,c):
    if(a>b and c>b):
        return (a+c)

    if(a==b and a==c):
        print(a+b)
        return(a+b)

    if(a<b and a<c):
        return(b+c)



def calculate_new_balance(balance,change):
    
    
    for i in change:
        if (i[2] == "deposit"):
            balance += i[1]
        if (i[2] == "withdrawal"):
            balance -= i[1]

    return(balance)



def list_n_perfect_square(num):
    count=0
    squaredList = []

    for i in range(num):
        count+=1
        squared=count*count
        squaredList.append(squared)

    return(squaredList)

def username_ends_with_digits(name):
    lastLetter = name[len(name)-1]
    if lastLetter.isdigit():
        return(True)
    else:
        return(False)

