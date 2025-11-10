#Find subarray with maximum product.

arr = [10,20,30,40,50]

max = arr[0]*arr[1]


for i in range(len(arr)-1):
    product = arr[i]*arr[i+1]
    
    if product > max: 
        max = product
  
        
print(f"The maximum among the product of subarray is {product}" )
    
