''''给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。

 

示例 1:

输入: [1,2,3]
输出: [1,2] (当然, [1,3] 也正确)
示例 2:

输入: [1,2,4,8]
输出: [1,2,4,8]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-divisible-subset
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        # print(nums)
        res = []
        return self.dfs(nums, 0, res, 0)


    def dfs(self, nums, i, res, max):
        if i == len(nums):
            print("i == len(nums):", res)
            return res
        # print(nums, i, nums[i] % res[-1] == 0, res)
        if len(res) == 0 or (nums[i] % res[-1]) == 0:
            res.append(nums[i])
            self.dfs(nums, i+1, res, max)
            res.pop()
            self.dfs(nums, i + 1, res, max)


    def main(self):
        list = [1, 2, 4, 5,  8]
        self.largestDivisibleSubset(list)

if __name__ == '__main__':
    Solution().main()