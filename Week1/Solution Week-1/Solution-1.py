#Write a Python script to enter an y number and check its prime or not

number=int(input("Enter a number:"))
ans=True
for i in range(2,number):
    if(number%2==0):
        ans=False
        break

if(ans==True):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
