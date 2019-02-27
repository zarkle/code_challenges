# https://leetcode.com/problems/valid-anagram/description/
# https://leetcode.com/articles/valid-anagram/


# runtime: 1600 ms
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = list(s)
        for char in t:
            if char in s:
                s.remove(char)
            else:
                return False
        if len(s) > 0:
            return False
        return True


# runtime: 80 ms, 30%
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        return sorted(s) == sorted(t)


# runtime: 56 ms, 72%; memory: 13.2 MB, 35%
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        if len(s) != len(t):
            return False

        letters = {}
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        for char in t:
            if char not in letters:
                return False
            letters[char] -= 1
            if letters[char] == 0:
                del letters[char]

        if letters:
            return False
        return True


# test case: 'ab', 'a'
