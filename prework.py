# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below. 


def hello_name(user_name):
    print("Hello" + "_" + user_name.title())

hello_name('Priscilla')



#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    """Returns odd values from 1-100"""
    odds = []
    for value in range (1,101):
        if value % 2 == 1:
            odds.append(value)
    print(odds)

# Call function
first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    """Returns max number in a list"""
    # Define a list to store the numbers to compare
    max_number = a_list[0]

    # loop though numbers to compare which one is bigger
    # biggest number at the time gets stored until it fails the loop
    for num in a_list:
        if num > max_number:
            max_number = num
    return max_number

# Define the testing lisst
a_list = [9, 204.8, 99.3, 34.8, 6]

#Call function
print("The biggest number in the list is : ", max_num_in_list(a_list))


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year): 
def is_leap_year(a_year):
    # Error Checking
    if not isinstance(a_year, int):
        return "Not a valid input, please input a whole number integer"
    
    # Divisible by 4?
    if a_year % 4 == 0:

        # Divisible by 100?
        if a_year % 100 == 0:

            # Divisible by 400?
            if a_year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False

#Question 5

#Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    for i in range(len(a_list)):
        if not isinstance(a_list[i], int):
            return 'Not a valid input.  Please submit a list of integers'
        if i == 0:
            continue
        elif a_list[i] != a_list[i-1] + 1:
            return False
    return True

