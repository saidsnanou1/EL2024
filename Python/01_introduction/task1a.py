def count_four(lst):
    count = 0
    for i in lst:
        if i == 4:
            count += 1
    print("The number 4 in the list:", count)


# Example list
my_list = [1, 5, 4, 7, 4, 6]

# Calling the function
count_four(my_list)
