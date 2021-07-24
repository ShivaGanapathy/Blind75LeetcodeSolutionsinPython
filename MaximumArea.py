class Solution:
    #O(n^2) Brute Force Solution
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        output = 0
        
        prev_height = 0
        for horizontal_cut in horizontalCuts:
            prev_width = 0
            for vertical_cut in verticalCuts:
                current = (vertical_cut-prev_width)*(horizontal_cut-prev_height)
                output = max(output, current)
                prev_width = vertical_cut
            
            prev_height = horizontal_cut
                
                
        return output % 1000000007
            