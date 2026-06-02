class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            key = tuple(sorted(string))
            groups[key].append(string)

        return list(groups.values())