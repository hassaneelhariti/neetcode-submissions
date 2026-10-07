class Solution {
    public int getSum(int a, int b) {
        int r=0;
        while(b!=0){
            r=a^b;
            b=(a&b)<<1;
            a=r;
        }
        return a;
    }
}
