class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}

        for c in s:
            if c not in my_map:
                my_map[c] = 1
            else:
                my_map[c] +=1

        for ch in t:
            if ch not in my_map:
                return False
            else:
                my_map[ch] -= 1

        for value in my_map.values():
            if value !=0:
                return False


        return True



        