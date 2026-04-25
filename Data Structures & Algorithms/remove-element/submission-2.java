class Solution {
    public int removeElement(int[] nums, int val) {
        int swapIndex = nums.length - 1;
        int runnerIndex = 0;
        
        while(runnerIndex <= swapIndex){
            if (nums[runnerIndex] != val){
                runnerIndex += 1;
            } else {
                nums[runnerIndex] = nums[swapIndex];
                nums[swapIndex] = val;
                swapIndex--;
            }
        }

        return runnerIndex;
    }
}