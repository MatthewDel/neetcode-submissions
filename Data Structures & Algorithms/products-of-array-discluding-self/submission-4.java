class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] sol = new int[nums.length];

        int runner = 1;

        for(int i = 0; i < nums.length; i++){
            sol[i] = runner;
            runner = nums[i] * runner;
        }

        runner = 1;

        for(int i = nums.length - 1; i >= 0; i--){
            sol[i] = sol[i] * runner;
            runner *= nums[i];
            System.out.println(sol[i]);
        }

        return sol;

    }
}  
