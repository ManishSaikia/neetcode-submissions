class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for index,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stemp,sindex=stack.pop()
                result[sindex]=index-sindex
            stack.append((temp,index))
        return result