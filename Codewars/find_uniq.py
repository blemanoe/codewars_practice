def find_unique(arr):
    if arr[0] not in arr[1:]:
        return arr[0]
    if arr[-1] not in arr[:-1]:
        return arr[-1]
    for x in range(len(arr)):
        if arr[x] == arr[x+1]:
            continue
        elif arr[x] != arr[x+1]:
            if arr[x+1] == arr[0]:
                return arr[x]
            else:
                return arr[x+1]

if __name__ == "__main__":
    #print(len([1,2,3,4,5]))
    print(find_unique([3, 10, 3, 3, 3]))