"""
Lists:list are datatype and a datastructure which stores sequence of datatype which can be any object type and it's similar to array as string it can be access through indexing.while accessing if we try to out of length then it gives error(IndexError: list index out of range).like string slice we have list slice by str[start:end:stepCover] and it works similar to string.by list slicing we will get subarray.
Matrix:describe 2d list and it's usefull during image processing and machine learning.and [arr1[subarr1]]
Common list patterns:
.sort(),.reverse()and can be done by slicing with -1,also by slicing we can copy it
.range(start,end) prints the range in order.
"""
# li=[1,2,3,4,5]
# li2=["ee","ss","he"]
# li3=["ee","ss","he",1,2,3]
# print(li3[0])
# print(len(li3))
# amazon_cart=['notebooks','sunglasses','toys','grapes']
# amazon_cart[0]='newLaptop'#list are mutable
# print(amazon_cart[0:2])#array can be slicing
# # new_cart=amazon_cart#by this here we're including value of amazon_cart to new_cart and we're not copying it.
# new_cart=amazon_cart[:]#by this here we're including value of amazon_cart to new_cart and we're copying it now.
# new_cart[0]="gum"#it will change both list
# print(new_cart)
# print(amazon_cart)
# matrix=[
#     [1,2,3],
#     [3,4,5],
#     [6,7,8]
# ]
# print(matrix[1][2])#will print 0 th row and in 1 index
#listMethods:performs specific to that
basket=[2,3,4,56,1,2,3]
print(len(basket))
basket.append(100)#adds the element at last of list and don't create new list
basket.insert(0,9)#adds the element at desired index of list and don't create new list
basket.extend([103,102,200])#this is similar to append which is iterable and can append n elements and don't create new list.
print(basket)
basket.pop(1)#it removes the given index and return that elementif nothing there it return none by default it remove last elements
print(basket)
basket.remove(100)#it removes the given element but nothing return by default it remove  first occurennce
print(basket)
basket.clear()#it clear the list completely.
print(basket)
basket2=["a","b","c","d","e","f","e"]
print(basket2.index("a",0,4))#here it search the given value in range of starting and ending in this if that not found it gives error(ValueError: 'e' is not in list)
print("d" in basket2)#retrun boolean as it'll iterate over basket2 and check if present then return boolean value. and in can applied to string or array
print(basket2.count("e"))#returns no of occurence of element in array
print(sorted(basket2))#it sort the array and creates new array and original array is not changed almost same as copying slicing and doing sort it
basket2.sort()#sort the array and doesn't return new array it only modifies it.
print(basket2)
basket3=basket2.copy()#will copy the list and return new array
print(f'basket3 {basket3}')
basket2.reverse()
print(f'reversed {basket2}')
print(list(range(0,101)))
newst=' '.join(["h","a","a"])#in join inside need to iterable i.e list and join to string and can either use like this or assign it to newSt with the previous
print(newst)
#list unpacking:this is to unpack the list in our way by assigning normal variable and if we want next to can by *other(can be any name) and next d can assign it
a,b,c,*other,d=[1,2,3,4,0,5,6,7,8,10,9]
print(a)
print(b)
print(c)
print(other)
print(d)