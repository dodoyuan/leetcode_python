
# -*- coding:utf-8 -*-

# “student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”
class Solution:
    def ReverseSentence(self, s):
        # write code here
        temp = s.split(' ')[::-1]
        return ' '.join(temp)

s = Solution()
print s.ReverseSentence('student. a am I')