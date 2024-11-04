#global list_multiple

def main():
    print("Hello world")

#def solution(number):
#	return sum(num if (num % 3 == 0) or (num % 5 == 0) else 0 for num in range(number))

def solution(number):
    iterate = number
    sum = 0
    list_multiple = []
    if number < 0:
        return 0
    else:
        while 0 < number:
            if ((number % 5 == 0) or (number % 3 == 0)) and number != iterate:
                list_multiple.append(number)
                sum+=number
            number = number - 1
    print(list_multiple)
    return sum



if __name__ == "__main__":
    main()
    #solution(60)
    print(solution(30))
    #print(list_multiple)

