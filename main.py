def arithmetic_arranger(problems, show_answers=False):
    
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    arranged_problems = ""
    line1 = ""
    line2 = ""
    dashes = ""
    answers = ""
    
    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()
        
        # Check the operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if operands are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check the length of operands
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the width of the row for the current problem
        row_width = max(len(operand1), len(operand2)) + 2
        
        # Create the formatted rows
        line1 += operand1.rjust(row_width) + "    "
        line2 += operator + operand2.rjust(row_width - 1) + "    "
        
        
    
    return arithmetic_arranger