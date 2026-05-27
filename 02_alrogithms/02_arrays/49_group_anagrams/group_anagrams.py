from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            key = tuple(sorted(s))
            anagrams.setdefault(key, []).append(s)
        return list(anagrams.values())
