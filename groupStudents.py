import sys
import math
import random
from student import Student

def main(args):    
    if len(args) != 2:
        print("Add in a Student file then a TA file as command line arguements")
    men, women = split_students(args[0])
    total_students = len(men) + len(women)
    groups = [None] * math.ceil(total_students / 4)
    print(len(groups))
    print(total_students)
    distribute_women(women, groups)

def distribute_women(women, groups):
    pass

def distribute_men(men, groups):
    pass

def shuffle_groups():




def split_students(file_name):
    men = set()
    women = set()
    with open(file_name, 'r') as file:
        file.readline()
        for line in file:
            line = line.strip('"\n')
            name_end = line.find('"')
            data = [line[:name_end]] + line[name_end + 2:].split(',')            
            student = Student(data[0], data[1], data[2])
            
            if student.gender == 'm':
                men.add(student)
            else:
                women.add(student)
    return men, women


main(sys.argv[1:])
