class Solution {
    public boolean isAnagram(String s, String t) {
    
        if(s.length() != t.length()){
            return false;
        }

        int len = s.length();

        int[] charMap = new int[26];

        for(int index = 0; index < len; index++){
            charMap['z' - s.charAt(index)]++;
            charMap['z' - t.charAt(index)]--;
        }

        for(int temp: charMap){
            if(temp != 0){
                return false;
            }
        }

        return true;

    }
}
