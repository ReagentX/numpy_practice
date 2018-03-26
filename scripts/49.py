import numpy as np


np.random.seed(100)
arr = np.random.randint(0,10,size=(6, 10))
form = np.arange(arr.shape[1])

def solve(a, form):
    # Generate tuples of unique values like `([values], [counts])`
    num_counts_array = [np.unique(row, return_counts=True) for row in a]

    ''' This is dumb.
        There are two array compressions at work here
        The outer one:
            [... for values, counts in num_counts_array] 
        Iterates through each tuple in `num_counts_array`
        The inner one replaces the elipsis:
            [counts[np.where(values == c)[0][0]] if True in np.isin(values, c) else 0 for c in form]
        It iterates through the items in the form, checks if they are in values list using `np.isin(values, c)`, and 
        assigns the count for the index of that number in the values array using `np.where(values == c)[0][0]`
        We have to use `[0][0]` because np.where returns an array of tuples and we only want the first item in the first tuple 
    '''
    return [[counts[np.where(values == c)[0][0]] if True in np.isin(values, c) else 0 for c in form] for values, counts in num_counts_array]

print(f'{list(form)}\n')
solution = solve(arr, form)
for row in solution:
    print(row)
