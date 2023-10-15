#!/bin/python3

'''
challenge description: https://www.hackerrank.com/challenges/new-year-chaos

- input
tc1:
q = [2, 1, 5, 3, 4]
tc2:
q = [2, 5, 1, 3, 4]

- expected output
tc1:
3
tc2:
Too chaotic

'''

# solution 2:  O(log n)
def update(bit, idx, val):
    while idx < len(bit):
        bit[idx] += val
        idx += idx & -idx

def query(bit, idx):
    s = 0
    while idx:
        s += bit[idx]
        idx -= idx & -idx
    return s

def minimumBribes(q):
    n = len(q)
    bit = [0] * (n+1)
    cnt = 0
    for i, val in enumerate(q):
        if val - (i + 1) > 2:
            print("Too chaotic")
            return
        cnt += query(bit, n) - query(bit, val)
        update(bit, val, 1)
    print(cnt)

if __name__ == '__main__':
    q = [3, 2, 4, 1]    
    minimumBribes(q)