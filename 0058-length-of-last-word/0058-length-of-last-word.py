class Solution(object):
    def lengthOfLastWord(self, s):
      b = s.strip()
      c = b.split()
      return len(c[-1])
        