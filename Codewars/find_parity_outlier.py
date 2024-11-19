def find_outlier(integers):
    if integers[0]%2 == 0 and integers[1]%2 == 0:
        for x in range(len(integers)):
            if integers[x]%2 == 1:
                return integers[x]

    if integers[0]%2 == 1 and integers[1]%2 == 1:
        for x in range(len(integers)):
            if integers[x] % 2 == 0:
                return integers[x]

    if integers[0]%2 != integers[1]%2:
        if integers[1]%2 == 1 and integers[2]%2 == 1:
            for x in range(len(integers)):
                if integers[x] % 2 == 0:
                    return integers[x]
        else:
            for x in range(len(integers)):
                if integers[x] % 2 == 1:
                    return integers[x]

if __name__ == "__main__":
    print(find_outlier([160, 3, 1719, 19, 11, 13, 21]))