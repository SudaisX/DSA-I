import ast
lst = input()
lst = ast.literal_eval(lst)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        curr_val = lst[i]
        curr_pos = i
        
        while curr_pos > 0 and lst[curr_pos - 1] > curr_val:
            lst[curr_pos] = lst[curr_pos - 1]
            curr_pos -= 1
        
        lst[curr_pos] = curr_val
        print(lst)

lst = [1,3,5,7,2,6,25,18,13]
insertion_sort([1,3,5,7,2,6,25,18,13])