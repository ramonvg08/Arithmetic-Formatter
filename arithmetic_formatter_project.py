def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5 : 
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format"
        
        first_operand, operator, second_operand = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first_operand), len(second_operand)) + 2

        first_line.append(first_operand.rjust(width))
        second_line.append(operator + ' ' + second_operand.rjust(width - 2))
        dashes.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(first_operand) + int(second_operand))
            else:
                answer = str(int(first_operand) - int(second_operand))

            answers.append(answer.rjust(width))

    arranged_first_line = '    '.join(first_line)
    arranged_second_line = '    '.join(second_line)
    arranged_dashes = '    '.join(dashes)

    if show_answers : 
        arranged_answers = '    '.join(answers)
        arranged_problems = f"{arranged_first_line}\n{arranged_second_line}\n{arranged_dashes}\n{arranged_answers}"
    else: 
        arranged_problems = f"{arranged_first_line}\n{arranged_second_line}\n{arranged_dashes}"

    return arranged_problems


