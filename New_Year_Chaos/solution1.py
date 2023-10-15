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

# solution 1:  O(n)
def minimumBribes(q):
    c = 0
    for i, v in enumerate(q):
        if v - (i+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, v-2), i):
            c += q[j] > v        
    print(c)

if __name__ == '__main__':
    q = [3, 2, 4, 1]    
    minimumBribes(q)