class Solution {
    public int getSum(int a, int b) {
        while(b!=0){
            int r=a^b;
            b=(a&b)<<1;
            a=r;
        }
        return a;
    }
}
