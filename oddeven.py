def check_even(num):
    what_is_num = ""
    if num % 2 == 0:
        what_is_num = "even"
    else:
        what_is_num = "odd"

    return what_is_num


print(check_even(8))
