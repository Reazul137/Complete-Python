a = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]

#prints all elements in a which are less than 5

for i in a:
    if i<5:
        print(i)
        
#above code in one line
        print([i for i in a if i < 5])
        
#creates a new list a_new with all the numbers less than 5 from list a 
        
        a_new =[]
        for i in a :
            if i < 5:
                a_new.append(i)
                
                print(a_new)
                
                #ask the user for a number and return a list that contains only elements
                #from the original list a that are smaller that that number given by the user.
                
                num=int(input("Please enter a number : "))
                for i in a :
                    if i < num:
                        print(i)