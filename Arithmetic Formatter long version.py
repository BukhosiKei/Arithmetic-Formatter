#!/usr/bin/env python
# coding: utf-8

# In[6]:


def arithmetic_arranger(problems, *sum):
  if len(problems) > 5:
    return "Error: Too many problems."
    
  arranged_problems = []

  for index, value in enumerate(problems):
    # ["32", "+", "8"]
    operator = value.split(" ")

    if operator[1] not in '-+':
      return "Error: Operator must be '+' or '-'."

    if len(operator[0]) > 4 or len(operator[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    try:
      value_1 = int(operator[0])
      value_2 = int(operator[2])
    except ValueError:
      return "Error: Numbers must only contain digits."

    #Calculate length of each line
    longest_val = max(len(operator[0]), len(operator[2]))
    width = longest_val + 2

    # operator ["32", "+", "8"]
    # output = f"{operator[0]:>{width}}\n{f'{operator[1]}{operator[2]}':>{width}}\n{'-'*width}"
    
    L1 = f"{operator[0]:>{width}}"
    L2 = operator[1] + f"{operator[2]:>{width-1}}"
    d = '-' * width


    try:
      arranged_problems[0] += (' ' * 4) + L1
    except IndexError:
      arranged_problems.append(L1)

    try:
      arranged_problems[1] += (' ' * 4) + L2
    except IndexError:
      arranged_problems.append(L2)

    try:
      arranged_problems[2] += (' ' * 4) + d
    except IndexError:
      arranged_problems.append(d)

    if sum:
      ans = int(operator[0]) + int(operator[2]) if operator[1] == '+' else int(operator[0]) - int(operator[2])
      a = f"{str(ans):>{width}}"
      
      try:
       arranged_problems[3] += (' ' * 4) + a
      except IndexError:
        arranged_problems.append(a)

        
  output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
  output = output + f"\n{arranged_problems[3]}" if sum else output
  
  return output


# In[7]:


arithmetic_arranger


# In[8]:


arranged_problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
output = arithmetic_arranger(arranged_problems, True)
print(output)


# In[ ]:




