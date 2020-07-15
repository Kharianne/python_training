"""
Write a Python function to multiply all the numbers in a list.
"""
# Not flexible but working solution
original_list = [25, 654, 898, 54, 646, 6546, 546]
new_list = [x * 5 for x in original_list]  # list comprehension
multiplier = 10
new_list = [x * multiplier for x in original_list]


# function solution
def multiply_list(_list, multiplier):
    if isinstance(_list, list):
        return [x * multiplier for x in _list]


print(multiply_list(original_list, multiplier))
"""
Write function/functions to compute triangle circumference and determine if the triangle is correct triangle.
Function will take *args 
"""


def is_it_triangle(*args):
    if args[0] + args[1] <= args[2]:
        return False
    elif args[0] + args[2] <= args[1]:
        return False
    elif args[1] + args [2] <= args[0]:
        return False
    else:
        return True


def triangle_circumference(*args):
    if len(args) != 3:
        raise TypeError("Wrong number of arguments. Triangle has 3 sides.")
    if is_it_triangle(*args):
        return sum(args)
    else:
        raise TypeError("Not a valid triangle!")

#print(triangle_circumference(1, 2, 3))
#print(triangle_circumference(5, 7, 3))
#print(triangle_circumference(1))


"""
Write a function that calculate hotel cost stay. 
prices = {
    "Hilton": 2500,
    "FourSeasons": 2800,
    "LowBudget": 500,
    "Love": 1000
}
"""

PRICES = {
    "Hilton": 2500,
    "FourSeasons": 2800,
    "LowBudget": 500,
    "Love": 1000
}


def get_price(nights, hotel, prices=None):
    if not prices:
        global PRICES
        prices = PRICES
    if prices.get(hotel):
        try:
            nights = int(nights)
            return prices[hotel] * nights
        except ValueError:
            raise ValueError("Number of nights is not a number!")
    else:
        raise ValueError("Hotel was not found!")


# get_price("et", "Hilton")
# print(get_price(3, "Hilton"))
# print(get_price(3, "AWER"))
# print(get_price(3, "Test", prices={"Test": 100}))
