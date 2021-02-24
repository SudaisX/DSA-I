n = int(input())
base = int(input())

def base_converter(n, base):
    nums = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    remainder = n % base
    if remainder >= 10: remainder = nums[remainder]
    
    if n == 0:
        return ''
    else:
        return base_converter(n//base, base) + str(remainder) 

print(base_converter(n, base))