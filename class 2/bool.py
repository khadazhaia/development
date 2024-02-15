
# You are given a triangle with a side #1 of 4, base of 6, and side #2 of 3. 
# Create a brief python script that will determine the perimeter of the triangle. Comment your code

# 1. Print the perimeter
# formula perimeter of a traingle is P = a+b+c (a:side) (b:base) (c:side)

side_one = 4
base = 6
side_two = 3

perimeter = side_one + base + side_two
print(perimeter)

# 2. Using boolean operators is side #1 greater than the base?

bool_one = side_one > base 
print("Using boolean operators is side #1 greater than the base?", bool_one)

# 3. Using boolean operators is side #2 less than the base?

bool_two = side_two < base
print("Using boolean operators is side #2 less than the base?", bool_two)

# 4. Using boolean operators is base larger than or equal to side #1?

bool_three = base >= side_one
print("Using boolean operators is base larger than or equal to side #1?", bool_three)
