class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
    
        answer = [1] * len(nums)

        # Prefix products
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
        
