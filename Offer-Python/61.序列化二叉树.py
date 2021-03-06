## 题目描述
# 请实现两个函数，分别用来序列化和反序列化二叉树
# 二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
# 从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的
# 二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），
# 以 ！ 表示一个结点值的结束（value!）。
# 二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.ldr_list = []
        self.index = -1

    def Serialize(self, root):
        # write code here
        s = self.GetLDRStr(root)
        return s

    def GetLDRStr(self, pHead):
        if not pHead:
            self.ldr_list.append('#')
            return
        self.ldr_list.append(str(pHead.val))
        self.GetLDRStr(pHead.left)
        self.GetLDRStr(pHead.right)
        return ','.join(self.ldr_list)

    def Deserialize(self, s):
        # write code here
        if not s:
            return None
        self.index += 1
        ldr_list = s.split(',')
        if self.index >= len(ldr_list):
            return None
        pHead = None
        if ldr_list[self.index] != '#':
            pHead = TreeNode(eval(ldr_list[self.index]))
            pHead.left = self.Deserialize(s)
            pHead.right = self.Deserialize(s)
        return pHead

if __name__ == "__main__":
    s = Solution()
    result_s = '5,4,#,3,#,2'
    result_n = s.Deserialize(result_s)
    print(result_n)
    print(result_n.left)
    print(result_n.right)
    print(result_n.left.left)
    print(result_n.left.right)
    # print(result_n.right.left)
    print(result_n.right.right)