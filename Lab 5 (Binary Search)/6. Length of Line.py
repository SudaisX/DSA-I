import ast
points_list = input()
points_list = ast.literal_eval(points_list)
length = float(input())


def length_of_line(points_list, length):
    def distance(points):
        x = points[1][0] - points[0][0]
        y = points[1][1] - points[0][1]
        return round((x**2 + y**2)**(1/2), 2)
    
    low = 0
    high = len(points_list)-1
    while low <= high:
        mid = (low + high) // 2
        if length == distance(points_list[mid]):
            return mid
        elif length > distance(points_list[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(length_of_line(points_list, length))