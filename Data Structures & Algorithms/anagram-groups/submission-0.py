class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict: dict[str, List[str]] = {}

        for s in strs:
            s_sorted: str = "".join(sorted(s))

            if s_sorted not in anagrams_dict.keys():
                anagrams_dict[s_sorted] = [s]
                continue

            anagrams_dict[s_sorted].append(s)

        return list(anagrams_dict.values())
