#we find the max array sum using the dynamic programming 

def max_product_subarray(nums):
    if not nums: 
        return 0 
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range (1,len(nums)):
        num = nums[i]
        
        if(num<0):
            max_product, min_product= min_product, max_product
            
        #Update the max and min products 
        max_product = max(num, max_product*num)
        min_product = min(num, min_product*num)
        
        
        result = max(result, max_product)
        
        
    return result


#Example 
arr = [2,3,-2,4,-1]
print("Maximum product subarray:", max_product_subarray(arr))
        
        
    