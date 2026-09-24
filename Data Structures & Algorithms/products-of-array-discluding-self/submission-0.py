class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list: List[int] = [1] * len(nums)

        for i in range(len(nums)):
            n: int = nums[i]

            for j in range(len(product_list)):
                if i == j:
                    continue
                
                product_list[j] *= n
        
        return product_list