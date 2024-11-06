'''
You are going to be given an array of integers.
Your job is to take that array and find an index N where the sum of the integers to the
left of N is equal to the sum of the integers to the right of N.

If there is no index that would make this happen, return -1.
'''
def find_even_index(arr):
    position = 0
    for x in range(len(arr)):
        if sum(arr[:position]) == sum(arr[(position + 1):]):
            break
        else:
            position += 1
    if position == len(arr):
        return -1
    else:
        return position

if __name__ == "__main__":
    print(find_even_index([1,2,3,4,5,6]))