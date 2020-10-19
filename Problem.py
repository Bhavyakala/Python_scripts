# QUESTION

# We wish to train a machine learning algorithm on an array of floating-point numbers in the
# interval [0.0, 1.0). The data is horribly unbalanced (not evenly distributed) and we wish to
# filter the dataset to obtain a subset containing an equal number of values from each interval
# [0, 0.2), [0.2, 0.4), ... [0.8, 1.0), throwing away as little data as possible.
# Example input
# Input - 0.1,0.3,0.5,0.7,0.9,0.5 
# Output - 0.1,0.3,0.5,0.7,0.9 

# Input - 0.15,0.12,0.35,0.38,0.55,0.56,0.57,0.75,0.77,0.9,0.94 
# Output - 0.15,0.12,0.35,0.38,0.55,0.56,0.75,0.77,0.9,0.94

import sys

list_num_string = input("Input list of numbers sepearated by comma: ")

def balance(list_num_string):
    bucket = {0.0: [], 2.0:[], 3.0:[], 4.0:[]} # Stores numbers in different buckets

    list_num = [float(i) for i in list_num_string.split(',')] #converts string input to list of floats
    
    # Add numbers into different buckets
    for i in list_num:
        if (i*10)//2 not in bucket:
            bucket[(i*10)//2] = [i]
        else :
            bucket[(i*10)//2].append(i)

    # Taking avg and minimum of no of items in each bucket
    s=0
    mn = sys.maxsize
    for item in bucket.items():
        s+=len(item[1])
        mn = min(len(item[1]),mn)
    avg = s//5
    
    final_list = []

    #If any bcket is empty return None
    if mn<=0:
        return None
    
    pick_num = min(mn,avg) #no. of items to pick from a bucket
    
    for item in bucket.items():
        final_list.extend(item[1][:pick_num])

    return ','.join([str(i) for i in final_list])

print(balance(list_num_string))