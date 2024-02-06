
def palindrome(word):
       return word == word[::-1]
 

    

if __name__ == '__main__': 
    user_input = input()
    palindrome(user_input)
