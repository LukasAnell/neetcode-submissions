class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_counts: dict[int, int] = {}

        for n in nums:
            if n not in unique_counts.keys():
                unique_counts[n] = 1
                continue

            unique_counts[n] += 1

        return list(dict(sorted(unique_counts.items(), key=lambda item: item[1], reverse=True)).keys())[:k]
