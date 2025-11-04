# Finding maximum and minimum with in an array

def find_max(arr): 
    n = len(arr)
    max = arr[0]
    
    for i in range(0, n): 
        if(max <= arr[i]):
            max = arr[i]
    return max
    
def find_min(arr): 
    n = len(arr)
    min = arr[0]
    
    for i in range(0,n):
        if(arr[i]<min):
            min = arr[i]
    return min

user_input = input("Enter the space seperated arrays:")
arr  = list(map(int, user_input.strip().split()))

min = find_min(arr)

max = find_max(arr)

print(f"The Minimum element in an array is: {min}")
print(f"The Maximun element in an array is: {max}")

 
    