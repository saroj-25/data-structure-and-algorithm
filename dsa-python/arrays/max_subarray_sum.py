'''
Given a array of integer(can be positive, negative, or zero) find the contigious subarray with the largest sum and return the sum. 
Input: arr = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The maximum subarray is [4,-1,2,1] with sum = 6
'''

def max_subarray_sum(arr): 
    if not arr: 
        return 0 # empty array 
    
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        #Either extend the current subarray or start a new 
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum


user_input = input("Enter integer seperated by spaces")
arr = list(map(int, user_input.strip().split()))

result = max_subarray_sum(arr)
print("The Maximum sub array sum is ", result)