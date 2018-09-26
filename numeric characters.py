def f(n: int) -> int:
   
    if (n % 2 == 0):
        return 1
    return 0
 
count = 0
for i in range(100):
    count += f(i)
 
print(count) 
