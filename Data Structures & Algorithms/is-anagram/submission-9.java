class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()){
            return false;
        }

        int len = s.length();

        HashMap<Character, Integer> freq = new HashMap<>();

        for(int index = 0; index < len; index++){
            freq.put(s.charAt(index), freq.getOrDefault(s.charAt(index), 0) + 1);
            freq.put(t.charAt(index), freq.getOrDefault(t.charAt(index), 0) - 1); 
        }

        for(int value: freq.values()){
            if(value != 0){
                return false;
            }
        }

        return true;
    }
}
