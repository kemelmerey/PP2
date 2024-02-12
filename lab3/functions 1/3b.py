#Write a Python function that checks whether a word or phrase is palindrome or not. 
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(c for c in s.lower() if c.isalnum())
    
    # Compare the string with its reversed version
    return s == s[::-1]

# Example
print(is_palindrome('madam'))  
# Output: True
print(is_palindrome('hello'))  
# Output: False