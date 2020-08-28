# Given the list of customer segments below please create a new list of the names of the segments only using 
# (a) a for loop 
# (b) a list comprehension 
# (c) a map(). 
# List would look something like ['Wallstreet','Gambler','Parents'] but of course using each tool as listed above. segments = [{'name': 'Wallstreet', 'average_spend': 82.01}, {'name': 'Gambler', 'average_spend': 107.00}, {'name': 'Parents', 'average_spend': 10.52}]

segments = [{'name': 'Wallstreet', 'average_spend': 82.01}, {'name': 'Gambler', 'average_spend': 107.00}, {'name': 'Parents', 'average_spend': 10.52}]

names_list = []
for client in segments:
    names_list += [client["name"]]
    
print(names_list)

names_comprehension = [client["name"] for client in segments]

print(names_comprehension)

def append(src, dest):
    for item in src:
        dest += [item["name"]]
    
    return dest

names_map = []    
map(append(segments,names_map), segments)

print(names_map)