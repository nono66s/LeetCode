money=[11,1,22,34,5134,4465,345,234,234,234,55,22,22,6,5]

def change(lst):
    print('not same list set',list(set(lst)))
    return list(set(lst))  

#use set() to make the element in input list become unique and then return it into list form

a=change(money)

def count_max(lst):
    flag=0 #expected minimized num=0 
    for num in a:  
        print ('num',num)#to learn what will come out 
        b=lst.count(num) #calculate one of the element in the list has how many same element 
        if b > flag :  #to get the biggest repeat amount 
            flag = b      
    return flag-1 #-1 to prevent remove all



def delete(del_time):
    while del_time > 0: #get from the return of count_max()
        for i in a:
            if money.count(i) != 0: #prevent crash  because remove function  can't remove nonexist element 
                money.remove(i)
        del_time-=1
        if del_time == 0: #after delete return the result
            return money

print(count_max((money)))
temp=count_max((money))
print(delete(temp)) #test





'''
a=list(set(lst))
flag=0

print('a',a)
for num in a:
    print('num',num)
    b=lst.count(num)
    print('lst.count(num)',b)
    if b > flag :
        flag = b
        mode_num = num
        print('mode_num',mode_num)
        
        '''