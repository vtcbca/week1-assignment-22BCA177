#6.Write a python script to enter any string and print only part of string. Take input of start character and end character from user.


string=input("Enter a string:")
start=int(input("Enter start position:"))
end=int(input("Enter end position:"))
ans=string[start-1:end:]    
print(f"The part of the string '{string}' is '{ans}'")
