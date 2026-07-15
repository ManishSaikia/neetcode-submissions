class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        result=0
        left=0
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            result=max(result,(right-left+1))
        return result