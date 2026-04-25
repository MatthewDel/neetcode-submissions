class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        List<Integer> stack = new ArrayList<>();
        int[] sol = new int[temperatures.length];

        for (int i = temperatures.length - 1; i >= 0; i--){
            
            while (stack.size() != 0 && temperatures[stack.get(stack.size()-1)] <= temperatures[i]){
                stack.remove(stack.size()-1);
            }

            if (stack.size() == 0){
                sol[i] = 0;
            } else {
                sol[i] = stack.get(stack.size()-1) - i;
            }

            stack.add(i);

        }

        return sol; 

    }
}
