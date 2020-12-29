# To get the highest even
# 


num_list = [11,10,2,3,4,8,16,20,100]

def highest_even(*arg):
    h_even = 0
    for i in num_list:
        if i % 2 == 0 and i > h_even:
            h_even = i
    return h_even        

print(highest_even(num_list))

