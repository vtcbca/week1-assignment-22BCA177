#.Write a python script to enter any number and print the sum of its digit.
  
number=int(input("Enter a number:"))
rem=0
sum=0
while(number!=0):
    rem=number%10
    sum=sum+rem
    number=number//10
print(f"The sum is {sum}!")  
    