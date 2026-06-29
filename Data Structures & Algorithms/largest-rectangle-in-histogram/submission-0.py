class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_area=0
        stack=[]
        for index,height in enumerate(heights):
            start=index
            while stack and height<stack[-1][0]:
                sheight,sindex=stack.pop()
                width=index-sindex
                area=width*sheight
                max_area=max(max_area,area)
                start=sindex
            stack.append((height,start))
        while stack:
            sheight,sindex=stack.pop()
            width=n-sindex
            area=width*sheight
            max_area=max(max_area,area)
        return max_area