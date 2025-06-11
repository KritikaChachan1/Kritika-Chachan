"""value = 10
print(value)

_name = "Kritika"
print(_name)

_name1 = "Kritika"
print(_name1)"""

#if we want to hold them we triple the code

a = 10
b = 20
print(a+b)

name ,  age , height = "Alice", 25, 5.6
print(name , age , height)

first_name = "Alice"
age_1 = 25
_height = 5.6
print(first_name , age_1 , _height)

#if list is there it has to be in box bracket [Bob , 25 , 6.0] , Bob =  string , 25 =  integer , 6.0 = float
#tuple in () this bracket  (it can not be changed)
#Dictinary in {} this bracket

#Eg of list

fruits = ["apple","banana","cherry"]
print(fruits)

mixed_list = [1,"apple",3.14,True]
print(mixed_list)

#Eg of tuple

fruits = ("apple","banana","cherry")
print(fruits)

mixed_list = (1,"apple",3.14,True)
print(mixed_list)

#Eg of Dictionary

person = {"name": "Alice" , "age" : 30 , "is_employed" : True }
print(person)

"""#when list can be changed

list = [0,1,2,3]
list[1] = 10
print(list)

#when tuple can not be changed

list = (1,2,3,4)
print(list)
list(2) = 10
print(list)"""

# type casting 

"""#converting integer to string

age = 25
age_str = str(age)
print(age_str)
print(type(age_str))

#converting string to integer

num_str = "123"
num_int = int(num_str)
print(num_int)
print(type(num_int))"""

# Converting to boolean
age = 0
age = bool(age)  
# 1 is considered True
print(age) 
# Output: True

#string to float
str_num = "3.14"
num_float = float(str_num)
print(num_float)  
# Output: 3.14
print(type(num_float))
# Output: <class 'float'>

str_invalid = "abc"
num_float = float(str_invalid)
# This will raise ValueError