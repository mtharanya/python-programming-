def printNGE(arr): 
  for i in range(0, len(arr), 1): 
next = -1
        for j in range(i+1, len(arr), 
 if arr[i] < arr[j]: 
                next = arr[j] 
                break
