# To find the duplicate from the list

a_list = ['a','b','c','a','d','a','d','c','e','f','g','h','g']
# a_list = [1,2,3,2,4,5,44,66,44,33,66,7,7,10,10]

duplicate = []

for i in a_list:
    if a_list.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)

print(f'These are the duplicate values: {duplicate}')





# To find duplicates using comprehension

a_list = ['a','b','c','a','d','a','d','c','e','f','g','h','g']

duplicate = list(set([char for char in a_list if a_list.count(char)>1]))

print(f'The duplicate elements in a_list are : {duplicate}')