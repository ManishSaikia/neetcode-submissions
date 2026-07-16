class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        result=0
        left=0
        for right in range(len(s)):
            freq[s[right]]+=1
            if (right-left+1)-(max(freq.values()))>k:
                freq[s[left]]-=1
                left+=1
            result=max(result,(right-left+1))
        return result