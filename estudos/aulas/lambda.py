double = lambda x:x*2
add = lambda x,y: x + y
max_value = lambda x,y: x if x >y else y
min_value = lambda x,y: x if x < y else y
full_name = lambda first, last: first + " " + last 
is_even = lambda x:x%2 == 0 
age_check = lambda age : True if age>= 19 else False

print(double(2))
print(add(3, 4))
print(max_value(6, 7))
print(min_value(9, 8))
print(full_name("Spongebob", "Squarepants"))
print(is_even(5))
print(age_check(21))