class Solution:
    def maxArea(self, height: List[int]) -> int:
        Area=0
        if len(height) == 0 :
            return Area
        if len(height) == 1:
            return Area

        for i in range (0,len(height)):
            start=height[i]
            for j in range (i+1,len(height)):
                end=height[j]
                if end >= start:
                    Area=max(Area,start*(j-i))
                else:
                    Area=max(Area,end*(j-i))
        return Area

class Solution:
    def maxArea(self, height: List[int]) -> int:
        Area=0
        door=0
        if len(height) == 0 :
            return Area
        if len(height) == 1:
            return Area

        for i in range (0,len(height)):
            start=height[i]
            if start > door:
                door=start
                for j in range (i+1,len(height)):
                    end=height[j]
                    if end >= door:
                        Area=max(Area,start*(j-i))
                    else:
                        Area=max(Area,end*(j-i))
        return Area
                        
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        Area,l,r=0,0,len(height)-1
        while r>l:
            Area = max(Area,min(height[l],height[r])*(r-l))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return Area

class Solution:
    def maxArea(self, height: List[int]) -> int:
        Area,floor,l,r=0,0,0,len(height)-1
        while r>l:
            Area = max(Area,min(height[l],height[r])*(r-l))
            if height[l]>height[r]:
                floor=height[r]
                while floor >= height[r]:
                    if r==l:
                        break
                    r-=1
            else:
                floor=height[l]
                while floor >= height[l]:
                    if l==r:
                        break
                    l+=1
        return Area