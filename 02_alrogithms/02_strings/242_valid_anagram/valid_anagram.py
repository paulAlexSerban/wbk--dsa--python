class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        set_ = set(s)
        if len(s) != len(t):
            return False
        for i in set_:
            if s.count(i) != t.count(i):
                return False
        return True
