# To test comprehension

#list comprehension
list1 = [char for char in 'jithammu']
list2 = [num for num in range(1,101)]
list3 = [num for num in range(0,101,2)]
list4 = [num**3 for num in range(1,101) if num % 2 ==0]

print(list1)
print(list2)
print(list3)
print(list4)

# set comprehension
set1 = {char for char in 'jithammu'}
set2 = {num for num in range(1,101)}
set3 = {num for num in range(0,101,2)}
set4 = {num**3 for num in range(1,101) if num % 2 ==0}

print(set1)
print(set2)
print(set3)
print(set4)

# dictionary comprehension
sample_dict = {
    'a': 1000,
    'b': 1500,
    'c': 2500
}

new_dict = {key:value*5 for key,value in sample_dict.items()}
new_dict2 = {key:value*5 for key,value in sample_dict.items() if value <= 1600}

print(new_dict)
print(new_dict2)