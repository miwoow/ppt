#!/bin/env/python
#encoding:utf-8

from numpy import random

MAX_INT = 50 

PATERN="%-13s"

def two_arg_problem():
    sel = '+'
    a = random.randint(1, MAX_INT-1)
    if random.randint(0, 1) == 0:
        sel = '+'
        if a < 10:
            b = random.randint(11-a, MAX_INT - a)
        else:
            b = random.randint(1, MAX_INT - a)
    else:
        sel = '-'
        if a > 10:
            b = random.randint(10, a)
        else:
            b = random.randint(1, a)

    problem = "%d%s%d=" % (a, sel, b)
    return PATERN % (problem)

def gen_next(a):
    sel = '+'
    b = 0
    result = a
    if a == 10:
        if random.randint(0, 1) == 0:
            sel = '+'
            b = random.randint(1, MAX_INT-a)
            result = a + b
        else:
            sel = '-'
            b = random.randint(1, a)
            result = a - b
    elif a < 10:
        sel = '+'
        b = random.randint(10-a, MAX_INT - a)
        result = a + b
    else:
        sel = '-'
        b = random.randint(a - 10, a)
        result = a - b

    return (result, "%s%d" % (sel, b))

def two_arg_problem_more():
    sel = '+'
    a = random.randint(1, MAX_INT-1)
    result, nex = gen_next(a)
    problem = "%d%s=" % (a, nex)
    return PATERN % (problem)


def three_arg_problem_more():
    a = random.randint(1, MAX_INT-1)
    result, nex = gen_next(a)
    result, nex2 = gen_next(result)

    problem = "%d%s%s=" % (a, nex, nex2)
    return PATERN % (problem)
 
def three_arg_problem():
    sel1 = '+'
    sel2 = '+'
    a = random.randint(1, MAX_INT-1)
    b = 0
    c = 0
    result = a
    if random.randint(0, 1) == 0:
        sel1 = '+'
        b = random.randint(1, MAX_INT - a)
        result = a + b
    else:
        sel1 = '-'
        b = random.randint(1, a)
        result = a - b

    if random.randint(0, 1) == 0:
        sel2 = '+'
        c = random.randint(0, MAX_INT - result)
        result = result + c
    else:
        sel2 = '-'
        c = random.randint(0, result)
        result = result - c

    problem = "%d%s%d%s%d=" % (a, sel1, b, sel2, c)
    return PATERN % (problem)
        

def do():
    problems = {}
    problem_list = []
    three_arg_num = random.randint(5, 8)
    line = ''
    line_num = 0
    j = 0
    for i in range(0, 50 - three_arg_num):
        new_problem = two_arg_problem_more()
        while new_problem in problem_list:
            new_problem = two_arg_problem_more()

        problem_list.append(new_problem)
        if problems.has_key(i/5):
            problems[i/5].append(new_problem)
        else:
            problems[i/5] = [two_arg_problem_more()]
        j = i+1

    for i in range(j, 50):
        new_problem = three_arg_problem_more()
        while new_problem in problem_list:
            new_problem = three_arg_problem_more()

        problem_list.append(new_problem)
        if problems.has_key(i/5):
            problems[i/5].append(new_problem)
        else:
            problems[i/5] = [new_problem]
    for i in problems.keys():
        print(''.join(problems[i]))

if __name__== '__main__':
    for i in  range(0, 4):
        print("日期：            班级：             姓名：")
        do()
