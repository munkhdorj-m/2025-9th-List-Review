# You can remove 'pass' if you written code in the function 

# Exercise 1
def sum_array(lst):
    total = 0
    for num in lst:
        total += num
    return total


# Exercise 2
def sum_positive(lst):
    total = 0
    for num in lst:
        if num > 0:
            total += num
    return total


# Exercise 3
def more_odds(lst):
    odd = 0
    even = 0
    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd > even:
        return "YES"
    return "NO"


# Exercise 4
def find_max(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum


# Exercise 5
def count_target(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count
