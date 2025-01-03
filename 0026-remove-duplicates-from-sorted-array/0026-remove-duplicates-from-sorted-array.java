class Solution {
    public int removeDuplicates(int[] nums) {
        HashSet<Integer>hs=new HashSet<>();
        int k=0;
        for(int i=0;i<nums.length;i++){
            if(hs.contains(nums[i])){
                continue;
            }
            else {
                hs.add(nums[i]);
                nums[k++]=nums[i];
            }
        }
        return k;
    }
}