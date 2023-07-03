#.Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.

number=input("Enter a number:")
if(number.isdigit()):
    b=str(number)
    if(b==b[::-1]):
        print("a palindrome number!!")
    else:
        print("not a palindrome number!!")
else:
    print(f"The input {number} is not valid!!")