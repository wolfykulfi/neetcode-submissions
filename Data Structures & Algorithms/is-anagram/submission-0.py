class Solution(object):
    def isAnagram(self, s, t):        
        if len(s) != len(t):
            return False
        letter = "abcdefghijklmnopqrstuvwxyz"
        for c in letter:
            if s.count(c) != t.count(c):
                return False
        return True