n=str(1010001)
print(list(n))
a=list(n)
print(a.count('1'))
#====================================================
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 10000000000000000000000000000000:
            temp=(n^0xffffffff)
            temp=list(str(bin( temp)))
            temp=temp.count('0')-1
            return temp
        else:
            temp=(n|0xffffffff)
            temp=list(str(n))
            temp=temp.count('0')
            return temp
#=====================================================

#a=10000000000000000000000000000000
b=int(bin(163912773132324367761611),2)
print(bin(163912773132324367761611))
def hammingWeight(n):
    num=0
    while n :
        if n & 1 :
            num+=1
        n>>=1
        print(n)          
    return num
        
#print('amount of 1 :', hammingWeight(a))
print('amount of 1 :', hammingWeight(b))


