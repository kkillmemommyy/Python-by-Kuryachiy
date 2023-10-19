from math import inf

def max_subsum(numbs):
    result = -inf
    current_sum = 0
    for n in numbs:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        if result < current_sum:
            result = current_sum
    return result
        

