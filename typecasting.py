#Assigning different variables
name= "Bunny"
Age= 15
is_student= True
Weight= 40.9

#Printing different Variables and their data types
print("Name: ", name)
print("Data type of name is", type((name)))

print("is_student :", is_student)
print("Data type of is_student is:", type((is_student)))

print("Weight:", Weight)
print("Data type of weight is: ", type((Weight)))

#Typecasting to convert the datatype of variables

print("\n After typecasting.....")
Age= str(Age)
print(Age)
print("Data type of age is:", type((Age)))


Weight= int(Weight)
print(Weight)
print("Data type of weight is:", type((Weight)))