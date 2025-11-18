# You have an array containing three types of elements (commonly 0, 1, and 2). You want to sort them in-place so that all 0s come first, then all 1s, and then all 2s, in one pass with O(n) time and O(1) space.

# This is called the Dutch National Flag problem, named after the red, white, and blue colors of the Netherlands flag.

def dutch_national_flag(arr):
    low =0
    mid =0
    high = len(arr)-1

    while mid<=high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid +=1

        else: 
            arr[mid], arr[high]=arr[high],arr[mid]
            high -= 1
    return arr 


arr = [2,0,2,1,1,0]
sorted_arr=dutch_national_flag(arr)
print(sorted_arr)