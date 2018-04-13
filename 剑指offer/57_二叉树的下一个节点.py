
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        if pNode.right:
            temp = pNode.right
            while temp.left:
                temp = pNode.left
            return temp
        temp = pNode
        while temp.next and temp != temp.next.left:
            temp = temp.next
        return temp.next

class Solution1:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        if pNode.right:
            temp = pNode.right
            while temp.left:
                temp = pNode.left
            return temp
        temp = pNode
        while temp.next:
            if temp is temp.next.left:
                   return temp.next
            temp = temp.next
        return temp.next
