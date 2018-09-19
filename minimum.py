while True:
    inp = raw_input('Enter a number: ')
    if inp == 'done' : 
        break

    try:
        num = float(inp)
    except:
        print 'Invalid input'
        continue                            

numbers = list(num)
minimum = None       


for num in numbers :                          
    if minimum == None or num < minimum :
        minimum = num

   print 'Minimum:', minimum



