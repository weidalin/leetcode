'''

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # global result
        result = []
        self.dfs(k, n, 1, [], result)
        return result

    def dfs(self, k, n, curr, num_array, res):
        if len(list(num_array)) == k and sum(list(num_array)) == n:
            res.append(list(num_array))
            return

        if len(num_array) > k or curr > 9:
            return

        for i in range(curr, 10):
            num_array.append(i)
            self.dfs(k, n, i+1, num_array, res)
            num_array.pop()



    def main(self):
        k=3
        n=9
        print(self.combinationSum3(k,n))



if __name__ == '__main__':
        Solution().main()

