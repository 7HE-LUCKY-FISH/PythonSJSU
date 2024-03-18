def is_palindrome(input_str: str) -> bool:
    stack = list(input_str)#string version
    reversed_str = ''.join(stack[::-1])
    return input_str == reversed_str

userword=input("Enter a word: ")
if(is_palindrome(userword)):
    print("Is a palindrome")
else:
    print("Is not a palindrome")



    '''
        STACK WAY OF DOING CODE
                stack = []
    for char in input_str:
        stack.append(char)

    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return input_str == reversed_str'''