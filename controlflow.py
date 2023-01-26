"""
In every program there is a way to control the flow of executing the programs and i.e by using conditional where expression are getting evaluated and it executes when that expressio run true and in python we have:
if condition:
    statement   this runs when if becomes true
if condition:
    stmt1
elif condition:
    stmt2
elif condition:
    stmtn
else:
    stmt      Here from line 5-11 runs when the execution is true else it executes line 12
if condition:
    stmt
else:
    stmt here it prints when expression evaluates to get false
we have and keyword in python to check mutliple condition in single line.
indentation are normal in programs for styling  but in python it's given to create a block of code for specific and by default it takes 4 indentation  
Truthy and Falsy:
In python everything what we define as variable will converts into Bool to Truthy value so it cares only True or False and falsy values like none ,0,"",[],{},()
"""
is_drive=True
is_licensed=True
if is_drive and is_licensed:
    print("You're elgible to drive has you have licenced")
else:
    print("You're not elgible to drive")
print("This prints after checking above")
#ternary operator:condition_if_true if condition else conditionalelsestmt(shortand of if-else) 
is_friend=False
can_message="message allowed" if is_friend else "not allowed"
print(can_message)
#short circuiting :It's nothing but it stops execution at begining itself when the condition is either true or false when using or ,and .
#logical Operator
print(9>8)#can have multiple expresion here
print(1==1)
print(8<9)
print(6>=6 and 8==8)
print(1==0 or 9>8)
print(0 !=0)
print(0<=0)
print(not False)

#is v/s ==(checks for both datatype and values)
print(True==1)#True
print(''==1)#False
print([]==1)#False
print(10==10.0)#False int==float->True
print([]==[])#False   samedatatype==samedatatype->true 
#is-> it checks for location in memory this value is stored is the same so it gives false  and datatype like string and number are stored in same memory location but list isn't stored in same location. is(strictly comparision operator)