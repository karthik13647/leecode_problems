class Solution {
    public int removeDuplicates(int[] nums) {
        HashSet<Integer> hs=new HashSet<>();
        int x=0;
        for(int i=0;i<nums.length;i++){
            if(hs.contains(nums[i])){
                continue;
            }
            else{
                hs.add(nums[i]);
                nums[x]=nums[i];
                x++;
            }
        }
        return x;
    }
}