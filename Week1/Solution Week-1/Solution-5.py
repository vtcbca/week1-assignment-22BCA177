##5.Write a python script to enter any string and count vowel.

strig=input("Enter a string:")
count=0
vowels=('a','e','i','o','u','A','E','I','O','U')

for i in strig:
    if i in vowels:
        count=count+1
print(f"The vowels count in '{strig}' is {count}")
    