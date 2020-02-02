class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        return helper(nums,0,0,S);
    }
    
    public int helper(int[] lst, int idx, int t, int s){
        if (idx == lst.length){
            if (s == t){
                return 1;
            }else{
                return 0;
            }
        }else{
            int count = 0;
            count += helper(lst,idx+1,t+lst[idx],s);
            count += helper(lst,idx+1,t-lst[idx],s);
            return count;
        } 
    }
}
