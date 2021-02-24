def popular_author(b):
    authors = {each['author']:0 for each in b} 
    for each in b:
        authors[each['author']] += 1  
        
    highest = 0
    for count in authors.values():
        if count > highest:
            highest = count
            
    popular = sorted([author for author, count in authors.items() if count == highest])
    return ', '.join(popular)
        
    
b = eval(input().strip())
print(popular_author(b))