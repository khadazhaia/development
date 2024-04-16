from statistics import mode

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''
# How do we create a dictionary?
user_data = {"user id":400, 
             "name":"Fritz",
             "address":"1515 Mockingbird Lane"}

# print(user_data)
# print(type(user_data))

# Access keys with brackets
# print(user_data["name"])
# print(user_data["user id"])
# print(user_data['address'])

# # Add new key value
# user_data["state"] = "NY"
# print(user_data)
# user_data["state"] = "NJ"
# print(user_data)

# lets look at all the methods available to us
# print(dir(user_data)) #dir let us look up all the methods 

# print(user_data.__contains__("user id")) #_contains_ outputs true if it in or false if it not in the dictionary

# print(user_data.__contains__("city"))

# lets try one
colors = ["blue", "green", "white"]
# print(dir(colors))

# Dict constructor
# new_dictionary = dict()
# print(new_dictionary)
# print(type(new_dictionary))

# pet_name = dict(name="Fido", age = 14)
# print(pet_name)
# print(type(pet_name))

# Dictionary methods

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets use the keys methods to get the keys from this dictionary
# Assign keys to a variable

dog_information = dog.keys()
# print(dog_information)
# print(dog.keys())

# Lets use clear method to remove all elements

# dog.clear()
# print(dog)

# Lets use get method to get a key value

age = dog.get("age")
# print(age)

# # # lets look at one of the parameters to show an error if the key doesnt exist
# print(dog.get("temperament", "Key does not exist"))

# Lets create a copy

new_dog = dog.copy()

# print(new_dog)
# print(type(new_dog))

# Lets remove a specified key with pop
# new_dog.pop("breed")
# print(new_dog)

# Lets remove a last inserted key-value pair with popitem
# new_dog.popitem()
# print(new_dog)

# Get a list with each key-value pair with items, will return a list of tuples
key_value_pairs_in_a_list_of_tuples = new_dog.items()
# print(key_value_pairs_in_a_list_of_tuples)

# we can loop through
# for k, v in new_dog.items():
#     print(k, v)

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}
# Update allows us to update by changing and adding data

dog.update({"temperament":"happy", "breed":"chihuahua"})
# print(dog)

# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}
 
# print(list1[3])
# print(dict1[3])

list1[3] = "z"
dict1[3] = "z"

# print(list1[3])
# print(dict1[3])

'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''
# Using a for loop; Hint, both of these lists happen to have the same length
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
new_dict = {}

# for n in range(len(list1)):
#      new_dict.update({list1[n]:list2[n]})
# print(new_dict)

# Using Zip & Dict
my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

# k_and_v = zip(my_keys,my_values)
# my_keys_and_my_values = dict(k_and_v)
# print(my_keys_and_my_values)

# solve it in one line of code
# my_dictionary = dict(zip(my_keys, my_values))
# print(my_dictionary)

# Using dictionary comprehension
my_dictionary = {keys: values for (keys, values) in zip(my_keys,my_values)}
# print(my_dictionary)

'''
Exercise

Write a dictionary that contains five words and their definitions. Then have your code print the word and their definition one at a time.
Hint: Use the items() method

'''

words = {"color":"blue", "veggie":"radish", "vehicle": "bike", "mood": "happy", "pet":"cat"}

# print(words.items())

# for k,v in words.items():
#     print(k, v)

# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}

# print(choices['flavors'][0])
# print(choices['sizes'][2])

'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''

car = {"make":"honda", 
       "model":"accord", 
       "year":2011 , 
       "number of doors":4,
       "cylinders": 6}

# print(car.items())

'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1] # our list

output = {} # my final output

# for m in my_list_items:
#     if m not in output:
#         output[m] = 1 # add it initially
#         # print(output)
#     else:
#         output[m] += 1 # updating the count
# print(output)

# Shorten the syntax
# for m in my_list_items: # looping through the list
#     output[m] = my_list_items.count(m)
# print(output)

# Statistics module
use_stats_module = [1,2,4,1,3,4,1,10,10,10,10]
result = mode(use_stats_module)
# print(result)

# Looping through and adding 
incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
total_incomes = 0.00

# for v in incomes.values():
#     total_incomes += v  # adding the income each time through
# print(total_incomes)

# adding without looping
# print(sum(incomes.values())) 

'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000},
           {'name': 'Alice', 'title': 'consultant', 'salary': 25000},\
           {'name': 'David', 'title': 'consultant', 'salary': 40000}]









 



