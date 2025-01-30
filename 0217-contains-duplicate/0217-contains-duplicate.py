class Solution(object):
    def containsDuplicate(self, nums): 
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return True
        return False
        