class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_one = 0
        word_two = 0
        result = [''] * (len(word1) + len(word2))
        insert_index = 0 
        while word_one < len(word1) and word_two < len(word2):
            result[insert_index] = word1[word_one]
            insert_index += 1
            result[insert_index] = word2[word_two]
            insert_index += 1
            word_one += 1
            word_two += 1
        
        while word_one < len(word1):
            result[insert_index] = word1[word_one]
            insert_index += 1
            word_one += 1
        
        while word_two < len(word2):
            result[insert_index] = word2[word_two]
            insert_index += 1
            word_two += 1
        
        return ''.join(result)

