class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] = counter.get(ord(s[i]) - ord('a'), 0) + 1
            counter[ord(t[i]) - ord('a')] = counter.get(ord(t[i]) - ord('a'), 0) - 1

        for count in counter.values():
            if count != 0:
                return False

        return True