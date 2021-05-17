# Michael LaLonde

# Situations that will return an error:
# If there are too many problems supplied to the function. The limit is five, anything more will return:
# Error: Too many problems.
# The appropriate operators the function will accept are addition and subtraction. Multiplication and division will
# return an error. Other operators not mentioned in this bullet point will not need to be tested.
# The error returned will be: Error: Operator must be '+' or '-'.
# Each number (operand) should only contain digits. Otherwise, the function will return:
# Error: Numbers must only contain digits.
# Each operand (aka number on each side of the operator) has a max of four digits in width.
# Otherwise, the error string returned will be:
# Error: Numbers cannot be more than four digits.

def arithmetic_arranger(problems, show_answers=False):
    # first see if there is 5 or less problems, otherwise return an error
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = []
    first_digits = []
    second_digits = []

    # if # of problems wasn't greater than 5, check if each problem is + or - and all problems contain numbers
    for i in range(len(problems)):
        split_prob = problems[i].split()

        # check to see if the operator is + or -, otherwise, return an error
        if split_prob[1] == '+' or split_prob[1] == '-':
            operators.append(split_prob[1])
        else:
            return "Error: Operator must be '+' or '-'."

        # check to see if both numbers in the string are really numbers, otherwise, return an error
        if split_prob[0].isnumeric() and split_prob[2].isnumeric():
            first_digits.append(split_prob[0])
            second_digits.append(split_prob[2])
        else:
            return "Error: Numbers must only contain digits."

        # check to see if each number is no more than 4 charactes long
        if len(split_prob[0]) > 4 or len(split_prob[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # process the numbers and get the answers
    answers = []
    for i in range(len(problems)):
        if operators[i] == '+':
            answers.append(int(first_digits[i]) + int(second_digits[i]))
        else:
            answers.append(int(first_digits[i]) - int(second_digits[i]))

    # create the string to be returned
    arranged_problems = ""

    # create the first digit line
    for i in range(len(problems)):
        # if the number is bigger than the first, the amount of formatting spaces is equal to the
        # length of the second_digit number
        if len(second_digits[i]) > len(first_digits[i]):
            num_spaces = 1 + abs(len(first_digits[i]) - len(second_digits[i])) + 1
            arranged_problems += (" " * num_spaces)
        else:
            num_spaces = 2
            arranged_problems += (" "*num_spaces)
        # regardless print the first digit and the 4 spaces separating each problem
        arranged_problems += first_digits[i]
        if i != len(problems)-1:
            arranged_problems += "    "

    # add a new line
    arranged_problems += "\n"

    # create the operator and second digit line
    for i in range(len(problems)):
        arranged_problems += operators[i] + " "
        # if the second number is bigger
        if len(second_digits[i]) > len(first_digits[i]):
            num_spaces = 0
        else:
            num_spaces = abs(len(first_digits[i]) - len(second_digits[i]))
        arranged_problems += (" "*num_spaces) + second_digits[i]
        if i != len(problems)-1:
            arranged_problems += "    "
    # add a new line
    arranged_problems += "\n"

    # create the hyphen line
    for i in range(len(problems)):
        # 2 is for the operator and space after
        if len(first_digits[i]) > len(second_digits[i]):
            num_hyphens = 2 + len(first_digits[i])
        else:
            num_hyphens = 2 + len(second_digits[i])
        arranged_problems += ("-"*num_hyphens)
        if i != len(problems)-1:
            arranged_problems += "    "

    if show_answers:
        # add a new line
        arranged_problems += "\n"

        # create the answer line
        for i in range(len(answers)):
            if answers[i] < 0:
                num_spaces = 1
            else:
                num_spaces = 2
            arranged_problems += (" "*num_spaces) + str(answers[i])
            if i != len(answers) - 1:
                arranged_problems += "    "
    return arranged_problems


def main():
    print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
    # output should be
    #     32      3801      45      123
    #  + 698    -    2    + 43    +  49
    #  -----    ------    ----    -----
    #    730      3799      88      172


if __name__ == '__main__':
    main()
