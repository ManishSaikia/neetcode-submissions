class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Count=collections.defaultdict(int)
        s2Count=collections.defaultdict(int)
        for i in range(len(s1)):
            s1Count[s1[i]]+=1
            s2Count[s2[i]]+=1
        if s1Count==s2Count:
            return True
        left=0
        for right in range(len(s1),len(s2)):
            s2Count[s2[right]]+=1
            leftChar=s2[left]
            s2Count[leftChar]-=1
            if s2Count[leftChar]==0:
                del s2Count[leftChar]
            left+=1
            if s1Count==s2Count:
                return True
        return False