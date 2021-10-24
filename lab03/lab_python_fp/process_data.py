import json
import sys
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1


path = 'data_light.json'

with open(path, encoding='utf8') as f:
    data = json.load(f)


#@print_result
def f1(arg):
    return list(sorted(Unique(list(field(arg, 'job-name')), ignore_case=True)))


#@print_result
def f2(arg):
    return list(filter(lambda job: job.startswith('Программист'), arg))


#@print_result
def f3(arg):
    return list((map(lambda job: job + ' с опытом Python', arg)))


#@print_result
def f4(arg):
    arg = list(arg)
    salary = gen_random(len(arg), 100000, 200000)

    return [job + f', зарплата {salary} руб' for salary, job in zip(salary, arg)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
