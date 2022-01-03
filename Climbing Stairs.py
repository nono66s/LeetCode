class Solution:
    def climbStairs(self, n: int) -> int:
        temp=[1,1]
        for i in range(2,n+1):
            temp.append(temp[i-1]+temp[i-2])
        return temp[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        temp={0:1,1:1}
        for i in range(2,n+1):
            temp[i]=temp[i-1]+temp[i-2]
        return temp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        memo[0]=1
        memo[1]=1
        def fab (n):
            if n in memo:
                return memo[n]
            else:
                memo[n]= fab(n-1)+fab(n-2)
                return memo[n]
        return fab(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 :
            return 1
        if n == 1 :
            return 1   
        return self.climbStairs(n-1)+self.climbStairs(n-2)