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
        
        
    
    return arithmetic_arranger