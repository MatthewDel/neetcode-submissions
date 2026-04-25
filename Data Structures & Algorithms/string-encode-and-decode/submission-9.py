class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []

        for to_encode in strs:
            length_and_delimeter = str(len(to_encode)) + "#"
            encoded_string.append(length_and_delimeter)
            encoded_string.append(to_encode)
        
        return "".join(encoded_string)


    def decode(self, s: str) -> List[str]:
        iterating_index = 0
        sol = []
        while iterating_index != len(s):
            size_of_encoded_string = []
            while s[iterating_index] != '#':
                size_of_encoded_string.append(s[iterating_index])
                iterating_index += 1
            
            int_size_of_encoded_string = int("".join(size_of_encoded_string))
            string_to_append = s[iterating_index + 1: iterating_index + int_size_of_encoded_string + 1]
            sol.append(string_to_append)
            iterating_index = iterating_index + int_size_of_encoded_string + 1
        
        return sol
            


            
