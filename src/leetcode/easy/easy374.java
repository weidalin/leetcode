package leetcode.easy;
/*
猜数字游戏的规则如下：

每轮游戏，系统都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，系统会告诉你，你猜测的数字比系统选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1 : 你猜测的数字比系统选出的数字大
 1 : 你猜测的数字比系统选出的数字小
 0 : 恭喜！你猜对了！

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

public class easy374 {
    static int pick = 1;
    public static int guess(int n){

        if (n==pick)
            return 0;
        else if (n>pick)
            return -1;
        else
            return 1;
    }
    public static int guessNumber(int n) {
        //二分查找法
        int low = 0;
        int high = n+1;
        int mid = -1;
        int res = -1;
        while (low <= high){
//            mid = (low + high+1)/2;
            mid = low + (high - low)/2;
            //-1    mid>pick
            res = guess(mid);
            if (mid==-1)
                high = mid-1;
                //1 mid < pick
            else if (res==1)
                low = mid+1;
            else
                return mid;
        }
        return -1;

    }

    public  static void main(String[] args) {
        int n = 10;
        System.out.print(guessNumber(n));
    }

}
