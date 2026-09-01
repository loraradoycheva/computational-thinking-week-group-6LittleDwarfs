def solution_station_7(input) -> int:
    variables, operators = input
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
                print(next_op)
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

