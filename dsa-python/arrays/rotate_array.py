#Function to rotate arrary to the right by k position 

def rotate_right(arr, k): 
    n = len(arr)
    k = k%n #handles the rotation greater than the arrray size 
    return arr[-k:]+arr[:-k]

# Function to rotate array to the left by k position 

def rotate_left(arr, k): 
    n = len(arr)
    k = k%n
    return arr[k:]+arr[:k]


#Take an input from the user 

user_input = input("Enter array elements seperated by spaces:")
arr = list(map(int, user_input.strip().split())) 

#Take a number of rotation 

k = int(input("Enter the number of rotation:"))

direction = input("Enter direction (left/right):").strip().lower()

if direction == "left": 
    rotated = rotate_left(arr,k)
elif direction == "right": 
    rotated = rotate_right(arr,k)
else: 
    print("Enter direction in left or right")
    exit()

print("Rotated Array", rotated)
    