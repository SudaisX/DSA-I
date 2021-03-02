import ast
rectangle_records = input()
rectangle_records = ast.literal_eval(rectangle_records)
record_title = input()

def sort_rectangles(rectangle_records, record_title):
    for i in range(1, len(rectangle_records)):
        curr_val = rectangle_records[i]
        curr_pos = i
        
        while curr_pos > 0 and rectangle_records[curr_pos - 1][record_title] > curr_val[record_title]:
            rectangle_records[curr_pos] = rectangle_records[curr_pos - 1]
            curr_pos -= 1
        
        rectangle_records[curr_pos] = curr_val
    return rectangle_records

print(sort_rectangles(rectangle_records, record_title))