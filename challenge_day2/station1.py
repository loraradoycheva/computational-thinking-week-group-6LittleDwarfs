def solution_station1(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    
    value_1 = 0
    value_2 = 1
    for i in range(1,index):
        temp = value_1
        value_1 = value_2
        value_2 = temp + value_2

    return value_2