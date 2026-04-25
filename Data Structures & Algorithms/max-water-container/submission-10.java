

class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxArea = 0;
        while (left < right){
            int valueLeft = heights[left];
            int valueRight = heights[right];

            int calculatedArea = (right - left) * Math.min(valueLeft, valueRight);
            maxArea = Math.max(calculatedArea, maxArea);

            if (valueLeft < valueRight){
                left++;
            } else if (valueLeft > valueRight){
                right--;
            } else {
                right--;
                left++;
            }

        }

        return maxArea;
    }
}
