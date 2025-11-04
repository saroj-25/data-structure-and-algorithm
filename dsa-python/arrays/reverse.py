# Reverse elements in-place or using extra space.

##using reverse method

arr = [10, 23, 44, 55, 66, 32, 54]
arr.reverse()
print(f"Reversed array is : {arr}")


# Using slicing

arr = [50, 53, 34, 44, 21, 43]
reversed_array = arr[::-1]
print(f"The reversed array is {reversed_array}")

# using builtin reversed function

arr = [20, 40, 23, 43, 55, 32]
reversed_array1 = list(reversed(arr))
print("Reversed array using reversed function:", reversed_array1)


# manually reversing using a loop
arr = [60, 34, 32, 35, 22, 44]
reversed_arr2 = []

for i in range(len(arr) - 1, -1, -1):
    reversed_arr2.append(arr[i])

print("Reversed array is ", reversed_arr2)
