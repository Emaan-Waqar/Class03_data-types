#input a word
text= str(input("Enter a string: "))

#Reverse String
#Using set value as -1 to iterate in reverse
revText= text[::-1]
text= revText

print("Reverse of given string is: ")
print(text)