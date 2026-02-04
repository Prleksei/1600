def bigger_number(list): 
    bigger = 0  
    for i in list:
        if bigger < i:
            bigger = i
        print(bigger)
bigger_number([1, 2, 3, 4, 5])
