class Solution {
    public void sortColors(int[] nums) {
        int[] colors = new int[3];

        for(int i = 0; i < nums.length; i++){
            colors[nums[i]] += 1;
        }

        for(int i = 0; i < nums.length; i++){
            
            for(int j = 0; j < colors.length; j++){
                if (colors[j] != 0){
                    nums[i] = j;
                    colors[j] -= 1;
                    break;
                }
            }

        }

    }
}