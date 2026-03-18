class Solution {
    public int[] findErrorNums(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        int dup = 0;
        int miss = 0;
        for(int n : nums){
            if(!seen.add(n)){
                dup = n;
            }
        }
        for(int i=1; i<=nums.length; i++){
            if(!seen.contains(i)){
                miss = i;
            }
        }
        return new int[]{dup, miss};
    }
}