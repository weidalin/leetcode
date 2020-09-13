'''You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. '''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    list = [False, False, False, False, True, True, True, True]

    def isBadVersion(self, n):
        return self.list[n-1]

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分查找法
        low, hight = 1, n
        mid = (low + hight) // 2
        # mid 为bad 并且mid-1为good时退出循环
        while low < hight:
            mid = (low + hight) // 2
            if self.isBadVersion(mid) and not self.isBadVersion(mid - 1):
                return mid
            # 如果mid-1是bad,找左边
            if self.isBadVersion(mid - 1):
                hight = mid - 1
            # 如果mid是good,找右边
            elif not self.isBadVersion(mid):
                low = mid + 1
        return hight

    def main(self):
        list = [False, False, False, False, True, True, True, True]
        n = len(list)
        firstBadVersion_n = self.firstBadVersion(n)
        print("firstBadVersion_n: ", firstBadVersion_n)


if __name__ == '__main__':
        Solution().main()

