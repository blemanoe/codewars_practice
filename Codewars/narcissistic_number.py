
def narr(value):
    str_value = str(value)
    int_to_list_str = []
    for x in range(len(str_value)):
        int_to_list_str.append(str_value[x])
    return int_to_list_str

if __name__ == "__main__":
    print(narr(1234))