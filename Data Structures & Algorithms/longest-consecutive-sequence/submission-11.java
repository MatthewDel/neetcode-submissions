class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> inputSet = new HashSet<>();

        for(int num: nums){
            inputSet.add(num);
        }

        int max_value = 0; 

        for(int i = 0; i < nums.length; i++){
            if(inputSet.contains(nums[i] - 1)){
                continue;
            }

            int tempValue = nums[i];

            while(inputSet.contains(tempValue)){
                tempValue += 1;
            }

            max_value = Math.max(max_value, tempValue - nums[i]);
        }

        return max_value;
    }
}
