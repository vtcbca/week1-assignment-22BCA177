#.Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.

number=input("Enter a number!!:")
if(number.isdigit()):
    number=int(number)
    sum=0
    copy=number
    rem=0   
    while(number!=0):
        rem=number%10
        sum=sum+(rem**3)
        number=number//10
    if(copy==sum):
        print("an armstrong number!")
    else:
        print("not an armstrong number!")

else:
    print(f"Theinput is not valid number!!")