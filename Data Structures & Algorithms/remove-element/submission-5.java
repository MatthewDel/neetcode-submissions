class Solution {
    public int removeElement(int[] nums, int val) {
        int swapIndex = nums.length;
        int runnerIndex = 0;
        
        while(runnerIndex < swapIndex){
            if (nums[runnerIndex] == val){
                nums[runnerIndex] = nums[--swapIndex];
            } else {
                runnerIndex++;
            }
        }

        return swapIndex;
    }
}