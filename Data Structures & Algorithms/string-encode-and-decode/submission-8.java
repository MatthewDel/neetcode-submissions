class Solution {

    public String encode(List<String> strs) {
        String result = "";
        for(int i = 0; i < strs.size(); i++){
            String fetchedWord = strs.get(i);
            result += fetchedWord.length() + "#" + fetchedWord;
        }
        System.out.println(result);
        return result;
    }

    public List<String> decode(String str) {
        List<String> sol = new ArrayList<>();

        int index = 0;
        String number = "";
        while (index < str.length()){
            char characterAtIndex = str.charAt(index);

            if(characterAtIndex == '#'){
                int parsedNumber = Integer.parseInt(number);
                String extractedString = str.substring(index + 1, index + parsedNumber + 1);
                sol.add(extractedString);
                index = index + parsedNumber + 1;
                number = "";
                continue;
            }

            index += 1;
            number += characterAtIndex;
        }

        return sol;

    }
}
