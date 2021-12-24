money=[11,1,22,34,5134,4465,345,234,234,234,55,22,22,6,5]

def change(lst):
    return list(set(lst)) 

a=change(money)

def count_max(lst):
    flag=0
    for num in a:  
        b=lst.count(num) 
        if b > flag :
            flag = b      
    return flag-1

def delete(del_time):
    while del_time > 0:
        for i in a:
            if money.count(i) != 0:
                money.remove(i)
        del_time-=1
        if del_time == 0:
            return money

print(count_max((money)))
temp=count_max((money))
print(delete(temp))

