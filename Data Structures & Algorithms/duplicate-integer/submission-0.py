class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # create an empty hash set
        for num in nums:
            if num in seen:      # if we've already seen this number, it's a duplicate
                return True
            seen.add(num)        # otherwise, record it in the set
        return False             # if loop finishes, no duplicates found
