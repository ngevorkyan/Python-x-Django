
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def sum_of_digits_str(num_str):
    if num_str == "":
        return 0
    else:
        return int(num_str[0]) + sum_of_digits_str(num_str[1:])


print(sum_of_list([1,2,3,4,5]))
print(sum_of_digits_str('12345'))
