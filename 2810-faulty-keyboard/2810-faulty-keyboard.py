class Solution(object):
    def finalString(self, s):
        result=[]
        for cha in s:
            if cha == 'i':
                result.reverse()
            else:
                result.append(cha)
        return ''.join(result)