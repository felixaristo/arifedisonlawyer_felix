# Author Felix Aristo
# Python file for palindrome detection

def reverseWords(s): 
    return s[::-1]

def palindromeDetection(s):
    wordsReversed = reverseWords(s)
    
    if (s == wordsReversed):
        return True
    return False
    
palindromeDetection("abcba")

# Return True
