class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(count == Counter(t)[char] for char, count in Counter(s).items()) and len(s) == len(t)