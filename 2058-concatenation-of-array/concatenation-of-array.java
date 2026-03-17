class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[nums.length + nums.length];
        int i = 0;
        for(int n: nums){
            ans[i++] = n; 
        }
        for(int n: nums){
            ans[i++] = n;
        }

        return ans;
    }
}