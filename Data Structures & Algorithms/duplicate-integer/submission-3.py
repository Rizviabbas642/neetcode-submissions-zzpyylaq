class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i , j in  enumerate(nums):
            if j not in seen:
                seen.add(j)
            else:
                return True

        return False
        