alist=[-45,0,3,10,90,5,-2,4,18,45,100,1,-266,706]
largest, larger = alist[0], alist[0]
for num in alist:
    if num > largest:
        largest, larger = num, largest
    elif num > larger:
        larger = num
print larger
