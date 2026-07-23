class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='':
            return ''
        countT,window=defaultdict(int),defaultdict(int)
        for c in t:
            countT[c]+=1
        have,need=0,len(countT)
        res,reslen=[-1,-1],float('inf')
        left=0
        for right in range(len(s)):
            char=s[right]
            window[char]+=1
            if char in countT and window[char]==countT[char]:
                have+=1
            while have==need:
                if (right-left+1)<reslen:
                    res=[left,right]
                    reslen=(right-left+1)
                window[s[left]]-=1
                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have-=1
                left+=1
        left,right=res
        return s[left:right+1] if reslen!=float('inf') else ''