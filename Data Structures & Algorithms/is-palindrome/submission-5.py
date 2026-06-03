import math

class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        s_cleaned = ""
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                s_cleaned += letter
        
        length_of_s = len(s_cleaned) - 1

        if length_of_s == -1:
            return True

        middle = math.floor(length_of_s)
        start, end = 0, length_of_s
        print(s_cleaned)
        while start != middle: 
            if s_cleaned[start].lower() != s_cleaned[end].lower():
                return False
            print(s_cleaned[start].lower() + " = " + s_cleaned[end].lower())
            start += 1
            end -= 1
        return True
