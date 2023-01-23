"""
none:special type that exist and similar to null means nothing  and can assign to variable it's usefull to video game when there is nothing exist 
Dictionary(hashmap):it's dict in python which is also datatype or datastructure and it denotes by {} and inside it contain 'key':value pair and to access that we can access like dictionaryName['key'] if found then return value else it gives error(KeyError: 'school)"It's an unordered arrangement of data in key:value pair " 
Inside an dictionary it can include any type of data as value keep in mind that inside list can also contain dictionary.
why we have dictionary over list?As we need to make particular access through name and if we used in dictionary it'll be easy and based on our requirement we can make combine of it.
"""
racer_prop=None
print(racer_prop)
student={
    'name':"Abc",
    'std':[4,3]
}
print(student['std'][0])#to get inside of dictionary and as array access through index 
my_list=[
    {
        'name':'axy',
        'std':[3,4]
    },
    {
        'name':'acd',
        'std':[5,9]
    }
]
print(my_list[0]['std'][1])#like this data access if list contain dictionary
#keys:A dictionary must be immutable so often we define it through string rather than other type and this must be unique if it's not unique then it gives latest updation and leave before defined one.
#methods:if user dictionary has many date where we're not known about keys in that case we use methods because if we searched by key which's unkown then if it's wrong then it gives error(keyError) so to avoid we use methods.
user={
    'name':'AbCX',
    'ph_no':928299299,
    'sssd':False
}
print(user.get('address','Bangalore'))#return value if key found else it return default one as specified 'bangalore' in this case
#create a dict with dict() a=dict()#will give empty dictionary and later can arrange based on our requirement by 
student_1=dict(name="nsnbs")#key must be in variable name in this case
print(student_1)
print('addess' in user)#will print True if it's exist else False
print(user.keys())#return keys of  dictionary
print(user.values())#return values of dictionary
print(user.items())#return key:value pair
# print(user.clear())#print none if it's directly cleared but if we print dictionary after clear then it give empty dictionary
user2=user.copy()#copies the user to user2 variable and similar to normal function
print(user2)
print(user2.pop('sssd'))#it will remove the key in dictionary which is specified and return the value of it 
print(user.popitem())#removes the random means some "key":"value" pair
print(user.update({'name':'cyz'}))#will update key if found it update value of that key else it create new one.
"""
Tuples:is like a list which creates in ordered way but it's immutable if we try to change then ot gives error(TypeError: 'tuple' object does not support item assignment) and can make access it through index and it's denoted by () and also use in to search.
why do we need tuples?
If we don't need to change the list at that case we can use this tuple.
In tuple we cannot add methods like sort() gives error(AttributeError: 'tuple' object has no attribute 'sort'),reverse()  gives error(AttributeError: 'tuple' object has no attribute 'reverse') and etc.
in dictionary keys can be define with tuple.
"""
my_tuple=(1,2,3,4,4)
# my_tuple[0]=0
print(my_tuple)
print(my_tuple[0])
# my_tuple.sort()
# my_tuple.reverse()
print(my_tuple)
a,b,*others=(1,2,3,4,5)
print(a)
print(b)
print(others)#while print with * it prints like lists
print(my_tuple.count(2))#counts the number of occurence of given parameter
print(my_tuple.index(3))
print(len(my_tuple))
"""Set:is a collection of unordered unique values,if duplicates then it return only unique and it's denoted by {}
Note:we can typecasting with any datatype through datatyoe methods and we cannot indexing here.
"""
my_set={1,2,3,4,5,3}
print(type(my_set))
my_set.add(0)
my_set.add(10)#will add only unique value into set
print(my_set)
list_1=[1,2,3,3,4,5,5] 
#print unique elements
print(set(list_1))#parsing list to set
print(set)
new_set=my_set.copy()#will copy the all set into assigned
my_set.clear()#clear the set
print(my_set) 
print(new_set)
my_set1={1,2,3,4,5}
my_set2={4,5,6,7,8,9}
my_set3=my_set1.copy()
print(my_set1.difference(my_set2))#print the value which are different in two sets
my_set1.discard(5)#will discard given member and return none if we print it
print(my_set1)
my_set3.difference_update(my_set2)#same as difference but this update and gives only unique
print(my_set3)
print(my_set1.intersection(my_set2))#prints the intersection values if present
print(my_set1 & my_set2)#similar to intersection 
print(my_set1.isdisjoint(my_set2))#return boolean True if it hasn't common 
print(my_set3.union(my_set2))#will union and remove duplicates.
print(my_set3 | my_set2) #shortend for union
my_set4={4,5}
print(my_set4.issubset(my_set2))#return true if it contain only common values
print(my_set4.issuperset(my_set2))#return true if it contain all common value else false and here it print false as my_set4 not contain common values as my_set2
print(my_set2.issuperset(my_set4))#return true if it contain all common value else false and here it print True as my_set2 contain common values as my_set4