class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        amount=len(nums) 
        for i in range (0,amount):
           for j in range (i+1,amount): 
                if (target-nums[i])==nums[j]: 
                    return [i,j]
