class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> stack = new ArrayList<>();

        for (int i = 0; i < s.length(); i++){

            Character index = s.charAt(i);

            if (index == '(' || index == '{' || index == '[') {
                stack.add(index);
            } else {
                if (stack.size() == 0){
                    return false;
                }

                Character topOfStack = stack.remove(stack.size()-1);

                if ((index == ')' && topOfStack != '(') || (index == '}' && topOfStack != '{') || (index == ']' && topOfStack != '[')){
                    return false;
                }
            }

        }

        return stack.isEmpty();
    }
}
