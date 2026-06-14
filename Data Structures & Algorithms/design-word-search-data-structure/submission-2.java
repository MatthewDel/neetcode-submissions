class WordDictionary {
    Node initialNode = new Node();

    public void addWord(String word) {
        Node dummy = initialNode;

        for(int i = 0; i < word.length(); i++) {
            int index = 'z' - word.charAt(i);

            if (dummy.map[index] == null) {
                Node newNode = new Node();
                dummy.map[index] = newNode;
            }

            dummy = dummy.map[index];
        }

        dummy.endOfWord = true;
    }

    public boolean search(String word) {
        return recursiveSearch(this.initialNode, 0, word);
    }

    public boolean recursiveSearch(Node curr, int index, String word) {
        if (curr == null) {
            return false;
        }

        if (index == word.length()) {
            return curr.endOfWord;
        } 

        char character = word.charAt(index);

        if (character == '.') {
            boolean result = false;
            for (Node next : curr.map) {
                result |= recursiveSearch(next, index + 1, word);
            }
            return result;
        } else {
            int newIndex = 'z' - character;
            return recursiveSearch(curr.map[newIndex], index + 1, word);
        }
    }

    class Node {
        Node map[];
        boolean endOfWord;

        public Node() {
            this.map = new Node[26];
        }
    }
}
