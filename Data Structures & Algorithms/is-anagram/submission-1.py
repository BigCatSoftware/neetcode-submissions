class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}

        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
        
        for c in t:
            if c in char_count:
                char_count[c] -= 1
            else:
                char_count[c] = -1
            
        for i in char_count.values():
            if i != 0:
                return False
        
        return True
