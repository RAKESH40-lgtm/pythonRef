"""Str is a datatype in python which holds texts which is string so by that we can get sequence of characters a,it's declared by either singlequotes(''),doublequotes("")and for multiple lines can be define by triple single quotes('''hw
jsj''') 
String Concatenation :it's done by adding two valid string an d this works only for string data type in python if we try to add sting and int then it give type err """
name="rak"#by " " or ''
print(name)
print(type(name))
address='''
by this
triple single quotes
can write long lines
'''
print(address)
print("My Favorite place"+" Mysore")
# print("g"+2) #TypeError: can only concatenate str (not "int") to str
a=100 #initialized by int type
b=str(a) #convert to string type conversion
c=int(b) #convert to int type conversion
d=float(c) #convert to float type conversion
print(type(b))
print(type(c))
print(type(d))
greet="\twelcome He\'s nice and \n got you" #here \ is escape sequence by which we can add symbols by \t tab and \n newLine
print(greet)
#format String:to print the string in formatted way and without using + operator and type casting we can format our string like this it's introduced in Python3
name1="Rajesh"
rated=5
print(f'Hi this is {rated} rated customer Mr.{name1}')
#for python2 we use .format(variableName="value") or .format(values=>where index starts from 0) but during this {} must be empty
print('Hi this is {} rated customer Mr.{}'.format(rated,name1))
#String Indexing:As wkt string are sequence so we can make operation by indexing which starts from 0 till last and in python by -1 it will starts from end
newStr="012345678"
print(newStr)#prints whole string
print(newStr[0])#prints starting index o
#with this indexing we can do string  slicing by[startingIndex:endingIndex:stepover] by default steps=1 and start and end is 0 till last and with this string slicing it gives substring
print(newStr[0::])#starts from 0 till last
print(newStr[0:3:2])#here starts from 0 end at 3 with 2 steps i.e 02
print(newStr[::-1])#reverse the string.
#immutability:strings are immutable means we cannot change part of string  by indexing it give error(TypeError: 'str' object does not support item assignment) and can change by reassign it will create new space 
str1="hello"
print(str1)
str1="string"#this can be done by changing it
print(str1)
# str1[0]="s"#this gives an error(TypeError: 'str' object does not support item assignment)
#In python there will be a built-in function like print() and many by which we get lot of helpfull
greety="welcome"
print(len(greety))#prints the length of string and we can also make use of len() with slicing and looping
#string methods: there are several by which we can do specific for  string itself 
quote="to be or not to be"
print(quote.upper())#prints the capital of all characters
print(quote.capitalize())#prints the capital of first character
print(quote.lower())#will lower the string
print(quote.find('be'))#will return first occur index of that if not found it return -1
print(quote.replace('be','me'))#will replace the be to me and create new string and can store new variable
print(quote)#as it's immuatable it won't change the original string 