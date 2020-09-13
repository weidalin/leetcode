'''637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。



示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        global res, num
        res = []
        num = []
        self.dfs(root, 0, res, num)
        return [res[i]/num[i] for i in range(len(res))]

    def dfs(self, root, i, res, num):
        if root == None:
            return
        if len(res) <= i:
            res.append(root.val)
            num.append(1)
            self.dfs(root.left, i + 1, res, num)
            self.dfs(root.right, i + 1, res, num)
        elif len(res) > i:
            res[i] += root.val
            num[i] += 1
            self.dfs(root.left, i + 1, res, num)
            self.dfs(root.right, i + 1, res, num)

    def main(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root_right = root.right
        root_right.left = TreeNode(15)
        root_right.right = TreeNode(7)
        res = self.averageOfLevels(root)
        print(res)

if __name__ == '__main__':
        Solution().main()