class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int index = 0;index < nums.length; index++){
            int calc = target - nums[index];
            if(map.containsKey(calc)){
                return new int[]{map.get(calc), index};
            }

            map.put(nums[index], Math.min(map.getOrDefault(nums[index], index), index));
        }

        return null;
    }
}
