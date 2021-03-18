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

def smallest_absdiff_pairs(lst):
    insertion_sort(lst)
    differences = []
    min_diff = 2**256
    
    for i in range(len(lst)-1):
        if abs(lst[i+1] - lst[i]) < min_diff:
            min_diff = abs(lst[i+1] - lst[i])   
    for i in range(len(lst)-1):
        if abs(lst[i+1] - lst[i]) == min_diff:
            differences.append((lst[i], lst[i+1]))
            
    return differences

print(smallest_absdiff_pairs(lst))