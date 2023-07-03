#7.Write a python script to enter any string, replace vowel with its position number.
#For Example: input: Amit
#             output:0m2t

string=input("Enter a string:")
ans=''
vowels=('a','e','i','o','u','A','E','I','O','U')
for index,j in enumerate(string):
    if(j in vowels):
        ans+=str(index)
    else:
        ans+=j
    
print(f"The string '{string}' after change is '{ans}' ")