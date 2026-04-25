class WordDictionary:

    def __init__(self):
        self.start = Node()

    def addWord(self, word: str) -> None:
        def helper(node, word):
            if word == "":
                node.endWord = True 
                return
            if word[0] not in node.dict:
                node.dict[word[0]] = Node()
                helper(node.dict[word[0]], word[1::])
            else:
                helper(node.dict[word[0]], word[1::])
        helper(self.start, word)

    def search(self, word: str) -> bool:
        def helper(node, word):
            if word == "" and node.endWord == True:
                return True
            if word == "":
                return False
            if word[0] == ".":
                resultant = False
                for key in node.dict:
                    resultant = resultant or helper(node.dict[key], word[1::])
                return resultant
            elif word[0] not in node.dict:
                return False
            else:
                return helper(node.dict[word[0]], word[1::])
        return helper(self.start, word)
            

        
class Node:
    def __init__(self):
        self.dict = {}
        self.endWord = False 