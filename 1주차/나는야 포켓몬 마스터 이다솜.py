import sys

n, m = map(int, sys.stdin.readline().split())
name_to_id = {}
id_to_name = {}
for i in range(1, n + 1):
    input = sys.stdin.readline().strip()
    name_to_id[input] = i
    id_to_name[i] = input
quizs = [sys.stdin.readline().strip() for _ in range(m)]

def get_data_type(input):
    data_type = 'str'
    try:
        int(input)
        data_type = 'int'
    except:
        pass

    return data_type

for quiz in quizs:
    data_type = get_data_type(quiz)
    if data_type == 'int':
        print(id_to_name[int(quiz)])
    else:
        print(name_to_id[quiz])