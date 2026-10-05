class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxnum= nums[0]
        currsum= 0
        for i in range(len(nums)):
            currsum= currsum + nums[i]

            if currsum > maxnum:
                maxnum = currsum
            if currsum<0:
                currsum=0
        return maxnum