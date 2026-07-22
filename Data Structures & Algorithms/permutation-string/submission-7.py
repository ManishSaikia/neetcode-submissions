class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        countS1=defaultdict(int)
        countS2=defaultdict(int)
        for i in range(len(s1)):
            countS1[s1[i]]+=1
            countS2[s2[i]]+=1
        if countS1==countS2:
            return True
        left=0
        for right in range(len(s1),len(s2)):
            countS2[s2[right]]+=1
            leftChar=s2[left]
            countS2[leftChar]-=1
            if countS2[leftChar]==0:
                del countS2[leftChar]
            left+=1
            if countS1==countS2:
                return True
        return False