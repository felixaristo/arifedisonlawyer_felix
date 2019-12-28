# Author Felix Aristo
# Python file for palindrome detection

def palindromeDetection(s):
    wordsReversed = s[::-1]
    
    if (s == wordsReversed):
        return True
    return False
    
palindromeDetection("abcba") # Run the function

# Return True

palindromeDetection("Abcba") # Run the function

# Return False
