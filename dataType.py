"""
To learn Programs and become good programmer.
Terms,DataType(what can hold),Actions(perform) and Best Practice.
DataTypes:through which values are stored in variable and we make use of it by action(modify) it
int:stores number value
float:stores number value
optional complex (which holds real and imaginary) is a similar datatype in number
bool:stores true or value
str:store sequence of characters
list
tuple
set
dict
class->custom datattype
Specialized Data Type->used through modules
None->nothing in programming language.
variables:way to store information(data) which can use it later for certain action which can called by name and assign(binding values) and when action takes it search and gives answer and this stores in binary.Make variables in descriptive  
Rules For Variable:
1)snake_case:ex:hello_1
2)start with lowercase and underscore(don't create by two underscore)
3)letters,numbers,underscore
4)Case sensitive
5)Don't overwrite keyword
in python to represent the constant can be shown by capitalize
expression and statement:
expresion :piece of code that produce value
statement:entire single line which perform certain action (store or evaluate)
Augment assignment operator using by +=,-= by operator= can use only while modifying it but not for defining.
"""
#Numbers has int and float where int stores whole number and float stores decimal values by this datatype we can do actions like printing,modifying through certain calculation.
print(2+2)
print(9-2)
print(9/2)
print(3*2)
print(2//1)#give integer part of quotient
print(3%4)#give remainder 
print(5**2)#which is power of right number
#type checks the datatype and prints it which is also action 
print(type(9/2)) #type-float
print(type(2+2))#type-int
#Math function:This are built in available in python 
print(abs(-20))#return the absolute value
print(round(2.6))#print the rounding near value
#operator Precedence:to calculate it follows rule as bracket(),of **,Multiplication*or Division / ,addition + or subraction-
print((10-2)+2**1-1*2/2)
print(bin(2))#represent the number 2 in binary by bin()
print(int('0b10',2)) #it converts the base 2 number
user_iq="snakeCase"#snake_case
user_gual=user_iq#assign one variable to one and another.
print(user_iq)
a,b,c=1,2,3#stores multiple values
print(a)
print(b)
print(c)
#boolean:in Python it's bool where True or False and this boolean are useful when we do conditional for controlling the flow of our program and can handle it nicely.
name3="s"
is_exist=False
print(is_exist)
is_exist=True
print(is_exist)