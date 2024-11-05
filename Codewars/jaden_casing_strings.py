def to_jaden_case(string):
    list_strings = string.split()
    for x in range(len(list_strings)):
        list_strings[x] = list_strings[x].capitalize()
    return " ".join(list_strings)

if __name__ == "__main__":
    print(to_jaden_case("how can mirrors"))