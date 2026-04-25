class Solution:
    def encode(self, strings):

        encoded = ""

        for word in strings:

            encoded += str(len(word)) + "#" + word
        
        return encoded 

    def decode(self, string):

        sol = []

        i = 0

        while i < len(string):

            number = 0

            while string[i] != "#":

                number = number * 10 + int(string[i])

                i+=1 

            sol.append(string[i+1:i+number+1])

            i = i+number+1
            
        return sol


