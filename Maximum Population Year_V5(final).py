class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        def get_years(years):
            temp=[]
            for i in range(len(years)): 
                live=years[i][1]-years[i][0] #birth、death 
                for j in range(live):         
                    temp.append(years[i][0]+j)     
            return temp

        year_list=get_years(logs)

        def change(lst):
            return list(set(lst)) 

        years_changed=change(year_list)

        def count_max(lst):
            flag=0
            for num in years_changed:  
                temp_count_max=lst.count(num) 
                if temp_count_max > flag :
                    flag = temp_count_max
            del_time=flag-1
            return del_time

        def delete(del_time):
            if del_time == 0:
                return min(year_list)
            while del_time > 0:
                for i in years_changed:
                    if year_list.count(i) != 0:
                        year_list.remove(i)
                del_time-=1
                if del_time == 0:
                    return min(year_list)

        result=delete(count_max(year_list))
        return result