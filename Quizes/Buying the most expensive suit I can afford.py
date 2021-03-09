import ast
suits = input()
suits = ast.literal_eval(suits)
budget = int(input())

def findSalePrice(original_price, discount_rate):
    discount_price = original_price * (discount_rate/100)
    sale_price = original_price - discount_price
    return sale_price

def buy_expensive_suit(suits, budget):
    left = 0
    right = len(suits) - 1
    while left <= right:
        mid = (left + right) // 2
        discounted_price = (suits[mid][1] /100)*(100-suits[mid][2])
        if budget == discounted_price:
            return tuple([suits[mid][0], discounted_price])
        elif budget > discounted_price:
            left = mid + 1
        else:
            right = mid - 1
    if budget > (suits[0][1] /100)*(100-suits[0][2]):
        return tuple([suits[right][0], (suits[right][1] /100)*(100-suits[right][2])])
    else:
        return -1

suit_to_buy = buy_expensive_suit(suits, budget)