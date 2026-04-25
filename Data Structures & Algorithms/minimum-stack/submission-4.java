class MinStack {

    ArrayList<Integer> minStack = new ArrayList<>();
    ArrayList<Integer> stack = new ArrayList<>();
    
    public void push(int val) {
        
        if (minStack.isEmpty() || minStack.get(minStack.size() - 1) >= val){
            minStack.add(val);
        }

        stack.add(val);
    }
    
    public void pop() {
        if(minStack.get(minStack.size() - 1).equals(stack.get(stack.size() - 1))){
            minStack.remove(minStack.size() - 1);
        }

        stack.remove(stack.size() - 1);
    }
    
    public int top() {
        return stack.get(stack.size() - 1);
    }
    
    public int getMin() {
        return minStack.get(minStack.size() - 1);
    }
}
