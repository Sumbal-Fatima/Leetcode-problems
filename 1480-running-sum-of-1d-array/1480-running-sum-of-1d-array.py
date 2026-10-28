class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        array = []
        total = 0
        for i in nums:
            total += i
            array.append(total)
        return array

