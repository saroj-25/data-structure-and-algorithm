#Given an array of integers and a target sum find a continuous subarray that adds up to the given sum 

def subarray_with_sum(arr,target_sum): 
    start =0 
    current_sum = 0 
    
    
    for end in range(len(arr)): 
        current_sum+= arr[end]
        
        #shrink the window when sum is greater than the target 
        
        while current_sum > target_sum and start <end: 
            current_sum -= arr[start]
            start +=  1
            
        #check if sum found  
        if current_sum == target_sum: 
            print(f"Subarray found from index {start} to {end}: {arr[start:end+1]}")
            return 
        
        print("No subarray found with given sum ")
        
        
#Example 

arr = [1,4,5,6,7,8,9]
target_sum = 30 
subarray_with_sum(arr,target_sum)



