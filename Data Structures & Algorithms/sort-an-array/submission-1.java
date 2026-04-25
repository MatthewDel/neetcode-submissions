class Solution {
    public int[] sortArray(int[] nums) {
        if(nums.length == 0 || nums.length == 1){
            return nums;
        }

        int mid = nums.length / 2;

        int[] left = new int[mid];

        for(int i = 0; i < mid; i++){
            left[i] = nums[i];
        }

        int[] right = new int[nums.length - mid];

        for(int i = mid; i < nums.length; i++){
            right[i - mid] = nums[i];
        }

        int[] resultOne = sortArray(left);
        int[] resultTwo = sortArray(right);
        return merge(resultOne, resultTwo);
    }

    public int[] merge(int[] arr1, int[] arr2){
        int runnerOne = 0;
        int runnerTwo = 0;
        int insertionIndex = 0;

        int[] sol = new int[arr1.length + arr2.length];

        while(runnerOne < arr1.length && runnerTwo < arr2.length){
            if (arr1[runnerOne] <= arr2[runnerTwo]){
                sol[insertionIndex++] = arr1[runnerOne++];
            }else{
                sol[insertionIndex++] = arr2[runnerTwo++];
            }
        }

        while(runnerOne < arr1.length){
            sol[insertionIndex++] = arr1[runnerOne++];
        }

        while(runnerTwo < arr2.length){
            sol[insertionIndex++] = arr2[runnerTwo++];
        }

        return sol;
    }
}