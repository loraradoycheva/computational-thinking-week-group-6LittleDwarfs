def solution_station_4(x): 
    for i in range(2, x): #for every value between 1 and n
        if x%i == 0: #check if i divides n
            return False #if this is true, n is not prime
    return True if x > 1 else False #values less than 2 are not prime
