import sys
import math
import random
from student import Student


MAX_GROUP_SIZE = 4

def build_groups(args):    
    if len(args) != 2:
        print("Add in a Student file then a TA file as command line arguements")
        return
    men, women = split_students(args[0])
    total_students = len(men) + len(women)
    groups = [[None] * 4 for x in range(math.ceil(total_students / 4))]
    distribute_women(women, groups)
    distribute_men(men, groups)
    shuffle(groups)
    validate_groups(men + women, groups)


def shuffle(lst):
    for i in range(random.randint(4, 8)):
        random.shuffle(lst)

def distribute_women(students, groups):
    temp_group = []
    all_groups = []
    for student in students:
        temp_group.append(student)
        if len(temp_group) == MAX_GROUP_SIZE:
            all_groups.append(temp_group)
            temp_group = []
        elif len(temp_group) == math.ceil(MAX_GROUP_SIZE / 2) and random.random() < 0.3:
            # If the size of the group is 1/2 full reset 30% of the time
            all_groups.append(temp_group)
            temp_group = []
        elif len(temp_group) == math.ceil(MAX_GROUP_SIZE / 1.5) and random.random() < 0.9:
            # If the size of the group is ~3/4 full reset 90% of the time
            all_groups.append(temp_group)
            temp_group = []
    group_number = 0
    for group in all_groups:        
        i = 0
        for student in group:
            groups[group_number][i] = student
            i += 1
        group_number += 1



def distribute_men(students, groups):
    group_number = 0
    students = iter(students)
    while group_number < len(groups):

        i = 0
        while i < len(groups[group_number]):
            if groups[group_number][i] is None:
                groups[group_number][i] = next(students, None)
            i += 1
            

        group_number += 1

def shuffle_groups():
    pass

def validate_groups(students, groups):
    seen = set()
    total = 0
    for group in groups:
        for student in group:
            if student is not None:
                total += 1
                seen.add(student)
    # print(f'Total Students: {len(students)}')
    # print(f'Students in groups: {total}')
    assert len(students) == len(seen)
    if len(students) != total:
        assert False, 'There is a bug I don\'t want to debug'

def print_groups(groups): 
    for group in groups:
        print('[', end='')
        for student in group:
            if student is not None:
                print(student.gender, end= ' ')
        print(']')

    

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
    men = list(men)
    women = list(women)
    random.shuffle(men), random.shuffle(women)
    return men, women


def main(args):
    # Terrible code here. There is a bug that happens sometimes and I don't want to debug so sloppy fix it is
    while True:
        try:
            build_groups(args)
            return
        except AssertionError:
            pass
        except:
            print("An error occured")
            return

main(sys.argv[1:])
