#!/usr/bin/env python
# coding: utf-8

# In[1]:


def arithmetic_arranger(problems, sum=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    line1 = line2 = line3 = line4 = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        line1 += operand1.rjust(width) + "    "
        line2 += operator + " " + operand2.rjust(width - 2) + "    "
        line3 += "-" * width + "    "

        if sum:
            result = str(eval(problem))
            line4 += result.rjust(width) + "    "

    arranged_problems.append(line1.rstrip())
    arranged_problems.append(line2.rstrip())
    arranged_problems.append(line3.rstrip())

    if sum:
        arranged_problems.append(line4.rstrip())

    return "\n".join(arranged_problems)


# In[3]:


problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
output = arithmetic_arranger(problems, True)
print(output)


# In[ ]:




