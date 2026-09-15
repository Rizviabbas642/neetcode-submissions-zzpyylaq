class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mmap = {}

        for char in strs:
            key = "".join(sorted(char))

            if key not in mmap:
                mmap[key] = []
            mmap[key].append(char)


        return list(mmap.values())

        