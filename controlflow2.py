"""
Loops:It's powerful concept in programming language to do repetitive task we use this loops in python we have for in loop by syntax:
for variable_name in(checks the declared variable in)  where to run:
    statements
iterable work with string ,array ,tuple, collection of items and takes indentation and we can nest the loop
In nested loop first run outerloop and runs inside innerloop and works till innerloop and outerloop prints it then comes out.
"""
# print("iterable work for string")
# for item in "hello":
#     print(item)
# print("iterable work for list")
# for item in [1,2,3,4,5]:
#     print(item)
# print("iterable work for tupple")
# for item in (1,2,3,4,5):
#     print(item)
# for item in [1,2,3,4,5]:
    # for value in ["a","b","c"]:
        # print(item,value)
"""
iterables are nothing but which are iterates like string,dictionary,list ,tuple and sets.
for dictionary:
 dictionary_name.items()# 
 dictionary_name.keys()
 dictionary_name.values() and can iterate dictionary by this methods
 Note :numbers are not iterable
"""
user={
    "name":"Xyx",
    "addres":"Mysore",
    "is_valid":True
}
#Print the key 
for item in  user:
    print(item)
#print the  value pair
for item in user.values(): 
    print(item)
#print the key-value pair
# for item in user.items():
#     print(item)
# for item in user.keys():
#     print(item)
# for key,value in user.items():
#     print(key,"->",value)
#range():is a object which gives the starting and end inclusive numbers in a range and it recieve 3 parameter start,end,steps and in steps default is 1 if we need - then we need to change start and end value 
print(range(10))
#in loop variable_name can be anything
for item in range(10):
    print(item)
for item in range(10,1,-1):
    print(item)
print(list(range(3)))
#enumerate() is special function which return the object which has index and its corresponding value,it always take iteratable datatype by which we get index of item and whuch is usefull to find index of item
for i,char in enumerate('hello'):
    print(i,char)
for key,val in enumerate([1,2,3]):
    print(key,val)
for idx,val in enumerate(list(range(100))):
    if val==50:
        print(val,idx)
"""
whileloop: similar to loop but differnce is need to initial before and give condition inside while() then make sure to incre or decr based on condition if not then it gives infinite loop and it break loop if condition fails and it can have else block
"""
i=0
while(i<=10):
    print(i)
    i=i+1
# else:
#     print("done counting")
#when to use while and for loop:based on problem we need to select it ,when we have iterable we can go on to use for loop but for lot of and to use while if don't know no of loop break is usefull at true condition in while loop. and we can use conditional logic in loop 
#break:will break the execution of loop
#continue:when it hits that part then continue to the next loop iteration.
#pass:it pass the data so it usefull to avoid error and get think about it.
for item in list(range(5)):
    print(item) 
    if item==2:
        break
for item in list(range(5)):
    print(item) 
    if item==2:
        continue
for item in list(range(5)):
    pass