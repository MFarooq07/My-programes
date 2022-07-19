"""
Created by: Muhammad Farooq Memon
Role: Student
Institute: Union College
"""
def add( num1, num2):
    """
    the following program is a calculator that only focuses on the addition
    :param num1: any number that the user want to include in addition
    :param num2: other number that the user want to include in addition
    :return: returns the total sum of all the entered numbers
    """
    sum = float(num1) + float(num2)
    end_addition = False
    while end_addition is not True:
        is_another_number = input("Do you want to add another number\nPress 1 if 'YES' and any other number if 'NO'\n ")

        if float(is_another_number) != 1:
            end_addition = True
        else:
            print("Total is: ", sum)
            add_num = (input("Please enter another number that you want to add: "))
            sum+=float(add_num)

    print("Total of all the numbers: ",sum)


num1 = input("Enter the number you want to add:                    ")
num2 = input("Enter the number you want to add to the previous one:")

add(num1,num2)


if __name__ == "__main__":
    print("the code wil be executed twice since their is one comand below and the other one after the code is executed")
    num1 = input("Enter the number you want to add:                    ")
    num2 = input("Enter the number you want to add to the previous one:")
    add(num1, num2)





