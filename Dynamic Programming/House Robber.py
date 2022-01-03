class Solution:
    def rob(self, nums: List[int]) -> int:
        prv,pprv=0,0
        for i in nums:
            Curr=max(prv,pprv+i)
            pprv,prv=prv,Curr
        return Curr