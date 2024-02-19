#!/usr/bin/env python
# coding: utf-8

# In[11]:


import time
import random


# Step 1: Read the file and store data
data_list = []  # Master list to hold all data
with open('product_data.txt', 'r') as file:  # Replace 'data.txt' with your file name
    for line in file:
        # Assuming each attribute is separated by a comma
        parts = line.strip().split(',')  # Strip removes newline characters, split divides the line
        data_list.append(parts)

# Step 2: Separate data into four lists
ids = []  # List for IDs
names = []  # List for names
prices = []  # List for prices
categories = []  # List for categories

for item in data_list:
    
    ids.append(item[0])
    names.append(item[1])
    prices.append(item[2])
    categories.append(item[3])


def insert_data(id, name, price, category):
    ids.append(id)
    names.append(name)
    prices.append(price)
    categories.append(category)
    
def update_data(id, new_name, new_price, new_category):
    index = ids.index(id)  # Find index of the item to update
    names[index] = new_name
    prices[index] = new_price
    categories[index] = new_category
    
def delete_data(id):
    index = ids.index(id)
    del ids[index]
    del names[index]
    del prices[index]
    del categories[index]
    
def search_by_id(user):
    user=input("Enter the ID of th eitem u want to search")
    if user in ids:
        index = ids.index(user)
        return {'ID': ids[index], 'Name': names[index], 'Price': prices[index], 'Category': categories[index]}
    else:
        return 'Item not found'

def search_by_name(name):
    if name in names:
        index = names.index(name)
        return {'ID': ids[index], 'Name': names[index], 'Price': prices[index], 'Category': categories[index]}
    else:
        return 'Item not found'
    



# Assuming prices is a list of floats
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # pivot is a float from prices list
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

prices = [float(item[2]) for item in data_list] 


quick_sort(prices, 0, len(prices) - 1)
print("Sorted prices:", prices)


def run_quick_sort(arr):
    quick_sort(arr, 0, len(arr) - 1)
    for product in products:
        print(f'ID: {arr.ID}, Name: {arr.name}, Price: {arr.price}, Category: {arr.category}')


# Function to measure the time taken by quick sort for different types of data
def measure_quick_sort_performance():
    random.seed(42)  # Seed for reproducibility
    # Generate data
    data_already_sorted = list(range(1, 1001))
    data_reverse_sorted = list(range(1000, 0, -1))
    data_random = random.sample(range(1, 1001), 1000)

    # Sort already sorted data
    start_time = time.time()
    quick_sort(data_already_sorted, 0, len(data_already_sorted) - 1)
    time_for_already_sorted = time.time() - start_time

    # Sort reverse sorted data
    start_time = time.time()
    quick_sort(data_reverse_sorted, 0, len(data_reverse_sorted) - 1)
    time_for_reverse_sorted = time.time() - start_time

    # Sort random data
    start_time = time.time()
    quick_sort(data_random, 0, len(data_random) - 1)
    time_for_random = time.time() - start_time

    print(f"Time taken for already sorted data: {time_for_already_sorted} seconds")
    print(f"Time taken for reverse sorted data: {time_for_reverse_sorted} seconds")
   

# Execute the performance measurement function
#measure_quick_sort_performance()



#insert_data(4, 'Item D', 15.99, 'Category 4')
#delete_data()
#print(search_by_id(57353))

#print("Prices:", prices)


# Now you have four separate lists: ids, names, prices, categories
# You can print them to verify
#delete_data("40374")
#update_data("57353", "MACBOOK_name", 9999, "Electronics")


#delete_data("40374")

print("IDs:", ids)
print("Names:", names)
print("Prices:", prices)
print("Categories:", categories)
print(search_by_id(57353))

#measure_quick_sort_performance()
#quick_sort(prices)
#run_quick_sort()
#print("Prices:", prices)
#print("Sorted prices:", prices)

    
#quick_sort(prices, 0, len(prices) - 1)

#measure_quick_sort_performance()


    


# In[ ]:




