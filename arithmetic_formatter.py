import re

def arithmetic_formatter(problems, display_answer_boolean = False):
    
    line1 = ""
    line2 = ""
    dashes = ""
    answer = ""
    arranged_problems = ""
    
    if len(problems) > 5:
        print("Error: Too many problems.")
        return 'Error: Too many problems.'
    
    operator_regex = '[+-]'
    operand_regex = '[a-zA-Z]'

    for item in problems:

        error_message = (
            'Error: Numbers must only contain digits.' if re.search(operand_regex, item) else 
            None
        )

        if error_message:
            print(error_message)
            return error_message

        split_item = item.split(" ")

        first_number = split_item[0]
        operator = split_item[1]
        second_number = split_item[2]
        total = str(first_number + second_number)

        if operator not in operator_regex:
            print("Error: Operator must be '+' or '-'.")
            return "Error: Operator must be '+' or '-'."

        if max(len(first_number), len(second_number)) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return 'Error: Numbers cannot be more than four digits.'

        right_align_width = max(len(first_number), len(second_number))

        line1 += f'{first_number:>{right_align_width + 2}}    '
        line2 += f'{operator} {second_number:>{right_align_width}}    '
        dashes += f'{"_" * (right_align_width + 2)}    '

        if display_answer_boolean:
            total = int(first_number) + int(second_number)
            answer += f'{total:>{right_align_width + 2}}    '

    arranged_problems += f'{line1.rstrip()}\n'
    arranged_problems += f'{line2.rstrip()}\n'
    arranged_problems += f'{dashes.rstrip()}\n'

    if display_answer_boolean:
        arranged_problems += f'{answer.rstrip()    }'
    
    print(arranged_problems)

arithmetic_formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)