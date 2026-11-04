def check_order(numbers):
    ascending = True
    descending = True

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            ascending = False
        if numbers[i] > numbers[i-1]:
            descending = False

    if ascending:
        return 1
    if descending:
        return -1
    return 0

if __name__ == "__main__":
    list1 = [1,2,3,4]
    list2 = [4,3,2,1]

    print(check_order(list1))
    print(check_order(list2))
