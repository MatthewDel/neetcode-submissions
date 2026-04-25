class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int leftMax = height[0];
        int rightMax = height[right];
        int sol = 0;

        while (left < right){
            if (leftMax < rightMax){
                left++;
                leftMax = Math.max(height[left], leftMax);
                sol += leftMax - height[left];
            } else {
                right--;
                rightMax = Math.max(height[right], rightMax);
                sol += rightMax - height[right];
            }
        }

        return sol;
    }
}
