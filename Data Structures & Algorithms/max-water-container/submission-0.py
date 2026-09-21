class Solution:
    def maxArea(self, heights: List[int]) -> int:
        arr = []
        l = 0
        r = len(heights) - 1

        while (l<r):
            widht = r-l
            height = min (heights[l],heights[r])
            arr.append(widht*height)
            
            if heights[l]<heights[r]:
                l +=1
            else:
                r -=1


        return max(arr) 




