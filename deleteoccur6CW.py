order = [1,1,3,3,7,2,2,2,2]
max_e = 3

c = [x for i, x in enumerate(order) if order[:i].count(x) < max_e]
  
print(c)