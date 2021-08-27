import sys



def main(args):
    '''
    Command arguements
    [Common_file_prefix] Example: [1pm] for files 1pm.csv AND 1pm.html
    [csv_file_name, html_file_name] Example: 1pm.csv 1pm.html
    '''
    if len(args) == 1:
        file_start = args[0]
        csv_file_name = f'{file_start}.csv'
        html_file_name = f'{file_start}.html'
    elif len(args) == 2:
        csv_file_name = args[0]
        html_file_name = args[1]
    else:
        print("Invalid Number of parameters")
    csv = parse_csv(open(csv_file_name, 'r'))
    html = parse_html(open(html_file_name, 'r'))
    
    i = 0
    while i < len(csv) and i < len(html):
        csv_elem = csv[i].strip()
        html_elem = html[i].strip()
        assert csv_elem == html_elem, f'No match (CSV: {csv_elem} HTML: {html_elem}'
        i += 1
    
    assert i == len(csv) and i == len(html), 'No match (Different number of students)'
    print(f"All good! {html_file_name} has all students in {csv_file_name}.")
    

def parse_csv(file):
    file.readline()
    students = []
    for line in file:
        line = line.strip('"\n')
        cutoff_index = line.index('"')
        student = line[:cutoff_index]
        students.append(student)
    return sorted(students)

def parse_html(file):
    students = []
    for line in file:
        line = line.strip()
        if line.endswith("<br />") and line[0] != "<":
            students.append(line[:-6])
    return sorted(students)




if __name__ == "__main__":
    main(sys.argv[1:])
