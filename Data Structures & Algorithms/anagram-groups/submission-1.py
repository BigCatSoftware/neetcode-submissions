class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            # key = tuple(sorted(string))
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            groups[key].append(string)

        return list(groups.values())