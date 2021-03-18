import ast
lst = input()
lst = ast.literal_eval(lst)

def dist(pair1, pair2):
    return round(( (pair2[0]-pair1[0])**2 + (pair2[1]-pair1[1])**2 )**(1/2), 3)

def minimum_distance_pairs(lst):
    min_distances = []  
    min_dist = 99999
    
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i != j:
                d = dist(lst[i], lst[j])
                if d < min_dist:
                    min_dist = d
                    
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i != j:
                if dist(lst[i], lst[j]) == min_dist:
                    min_distances.append((lst[i], lst[j]))
    
    return min_distances
                    
print(minimum_distance_pairs(lst))