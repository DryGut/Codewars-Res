feast = 'chickadee'
dish = 'chocolate cake'

def comp():
  c = [i.split() for i in feast]
  b = [c[i][i] for i in (0, -1)]

  a = [i.split() for i in dish]
  d = [a[i][i] for i in (0, -1)]

  if b == d:
    return True

comp()