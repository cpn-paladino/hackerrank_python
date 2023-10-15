#!/bin/python3

'''
challenge description: https://www.hackerrank.com/challenges/minimum-swaps-2

- input
tc1:
arr = [4, 3, 1, 2]

- expected output
tc1:
3

'''

# solution 1:  O(n)
def minimumSwaps(arr):
    swp=0
    i=0
    while i < len(arr):
        j = arr[i]-1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            swp+= 1
        else:
            i+= 1
    return swp


if __name__ == '__main__':
    arr = [4, 3, 1, 2]    
    res = minimumSwaps(arr)
    print(res)