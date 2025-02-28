class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            num = nums[nums[i]]
            ans.append(num)
        return ans
        