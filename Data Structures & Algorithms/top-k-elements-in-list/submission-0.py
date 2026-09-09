class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr= []

        mmap = {}

        for index, value in enumerate(nums):
            if value not in mmap:
                mmap[value] = 1

            else:
                mmap[value] +=1

        arr = list(mmap.keys())
        arr.sort(key = lambda x:mmap[x], reverse = True)
        return arr[:k]

        

        