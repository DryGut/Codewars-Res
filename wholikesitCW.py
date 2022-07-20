names = ['Peter', 'John', 'Mary', 'James']

def likes(names):
    c = [i for i in names if names.count(i)]
    b = len(names[2:])
    
    if len(c) == 0:
        return 'no one likes this'
    elif len(c) == 1:
        return f"{str(c[0])} likes this"
    elif len(c) == 2:
        return '{} and {}'.format(c[0], c[1]) + ' like this'
    elif len(c) == 3:
        return f"{'{}, {} and {}'.format(c[0], c[1], c[2])} like this"
    elif len(c) > 0:
        return f"{'{}, {}'.format(c[0], c[1])} and {b} others like this"

likes()