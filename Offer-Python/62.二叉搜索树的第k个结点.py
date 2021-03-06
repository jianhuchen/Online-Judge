## 题目描述
# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如,
# （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.nodes = []

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.k = k
        if k <= 0 or not pRoot:
            return None
        self.GetLDRList(pRoot)
        try:
            return self.nodes[k-1]
        except:
            return None

    def GetLDRList(self, pHead):
        if not pHead:
            return
        # 截断
        if len(self.nodes) >= self.k:
            return
        self.GetLDRList(pHead.left)
        self.nodes.append(pHead)
        self.GetLDRList(pHead.right)