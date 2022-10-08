import collections
sequence = '46463464375846436467'
def count_it(sequence):
    c = collections.Counter(sequence).most_common(5)
    f = sorted(c)
    d = dict(f)
    
    return(d)
x = count_it(sequence)
print(x)

