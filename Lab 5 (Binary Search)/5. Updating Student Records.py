import ast
student_records = input()
student_records = ast.literal_eval(student_records)
ID = input()
record_title = input()
data = input()

def binary_search(lst, item):
    first, last = 0, len(lst)-1
    while first <= last:
        mid = (first + last) // 2
        if item == lst[mid][0]:
            return mid
        elif item > lst[mid][0]:
            first = mid + 1
        else:
            last = mid - 1
    return -1

def update_record(student_records, ID, record_title, data):
    def update(records, ID_index, title, data):
        records[ID_index] = list(records[ID_index])
        if title == 1: records[ID_index][title] = data
        else: records[ID_index][title] = int(data)
        records[ID_index] = tuple(records[ID_index])
        
    ID_index = binary_search(student_records, ID)
    if ID_index == -1:
        return 'Record not found'

    if record_title == 'ID':
        return 'ID cannot be updated'
    elif record_title == 'Email':
        update(student_records, ID_index, 1, data)
    elif record_title == 'Mid1':
        update(student_records, ID_index, 2, data)
    elif record_title == 'Mid2':
        update(student_records, ID_index, 3, data)
    return student_records
    

print(update_record(student_records, ID, record_title, data))