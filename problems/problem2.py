from collections import Counter


def solve(socks_array):
    counter = Counter(socks_array)
    return sum([count // 2 for count in counter.values()])
            
       

