def printAllKLength(set, k): 
  
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
  

def printAllKLengthRec(set, prefix, n, k): 
      
   
    if (k == 0) : 
        print(prefix) 
        return
  
   
    for i in range(n): 
  
        
        newPrefix = prefix + set[i] 
              printAllKLengthRec(set, newPrefix, n, k - 1) 
