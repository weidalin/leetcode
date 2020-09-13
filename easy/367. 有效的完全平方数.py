'''367. 有效的完全平方数
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #1+3+5+.....+m n项
        #sn= a1*n+(n-1)n*d/2
        #sn = 1*n+ (n-1)n
        #sn = n**2
        num1 = 1
        while(num>0):
            num -= num1
            num1 += 2
        return num == 0

    def isPerfectSquare2(self, num: int) -> bool:
        if num <=0 or int(num**0.5)**2 !=num:
            return False
        return True

    def main(self):
        num=16
        bool = self.isPerfectSquare2(num)
        print(bool)

if __name__ == '__main__':
        Solution().main()