def solution_station_7(input):
    variables = []
    operators = []
    temp = 0
    for char in input:
        if temp == 0:
            variables.append(char)
            temp = 1
        elif temp == 1:
            operators.append(char)
            temp = 0
        
    converted_vars = []
    a = 3
    b = -1
    c = 4
    d = 7
    e = 0.5
    
    for var in variables:
        match var:
            case "a":
                converted_vars.append(a)
            case "b":
                converted_vars.append(b)
            case "c":
                converted_vars.append(c)
            case "d":
                converted_vars.append(d)
            case "e":
                converted_vars.append(e)
            case _:
                return "Wrong input."
        
    
    
    
    calculation = 0
    solution = []
    next_op : str
    counter = 0
    
    
    if len(operators) + 1 == len(converted_vars):
        operators.append("placeholder for equal list length")
        for var in converted_vars:
            if counter == 0:
                calculation += var
                next_op = operators[counter]
                
            else:
                match next_op:
                    case "*":
                        calculation *= var
                        next_op = operators[counter]
                    case "/":
                        calculation /= var
                        next_op = operators[counter]
                    case "+":
                        solution.append(calculation)
                        calculation = converted_vars[counter]
                        next_op = operators[counter]
                    case "-":
                        solution.append(-calculation)
                        calculation = converted_vars[counter]
                        next_op = operators[counter]
                    case _:
                        return "Wrong input."
            counter += 1
    solution.append(calculation)
    final = 0
    for x in solution:
        final += x
    
    return final

print(solution_station_7("a+b"))