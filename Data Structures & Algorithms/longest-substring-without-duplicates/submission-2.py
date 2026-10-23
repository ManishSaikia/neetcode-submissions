class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, left = 0 , 0
        st = set()
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            result = max(result, right-left+1)
        return result
            
