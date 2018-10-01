string1 = input("Enter first string: ")
if string1 == 'x':
    exit()
else:
    string2 = input("Enter second string: ")
    if string1 == string2:
        print("Both strings are equal to each other.")
        print(string1,"==",string2);
 else:
        print("Strings are not equal.")
        print(string1,"!=",string2);
