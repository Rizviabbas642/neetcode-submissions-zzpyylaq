class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mmap = {}

        for index,value in enumerate (nums):
            diff = target - value

            if diff in mmap:
               return [mmap[diff], index]


            mmap[value] = index
        