import math

class Solution:
    def isPalindrome(self, s: str) -> bool:

        length = len(s)
        start = 0
        end = length - 1
        middle = math.floor(end)

        if length <= 1:
            return True

        while start <= middle:
            if s[start].isalpha() or s[start].isdigit():
                if s[end].isalpha() or s[end].isdigit():
                    if s[start].lower() == s[end].lower():
                        print(s[start].lower() , s[end].lower())
                        start += 1
                        end -= 1 
                    else:
                        return False
                else:
                    end -= 1
            else:
                start += 1
                
        return True   


