class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        l = len(heights)
        max_area = max(heights)
        if not heights:
            return 0 

        for idx in range(len(heights)):
            
            start = idx
            while stack and stack[-1][1] > heights[idx]:
                area = ((idx - stack[-1][0]) * stack[-1][1])
                i, h = stack.pop()
                max_area = max(max_area, area)
                start = i
            stack.append((start, heights[idx]))
            

        for e in stack:
            area = ((l - e[0]) * e[1])
            max_area = max(max_area, area)
        return max_area
       
            
            
        

