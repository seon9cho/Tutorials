# standard_library.py
"""Python Essentials: The Standard Library.
<Name>
<Class>
<Date>
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return min(L), max(L), sum(L)/len(L)


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    print("int is immutable, str is immutable, list is mutable, tuples are immutable, sets are mutable")


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than those that are imported from your
    'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    import calculator as cal
    return cal.math.sqrt(cal.sum(cal.product(a, a), cal.product(b, b)))


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    from itertools import combinations
    p1 = []
    for i in range(len(A)+1):
    	p1 += list(combinations(A, i))
    p2 = []
    for i in range(len(p1)):
        p2.append(set(p1[i]))

    return p2


# Problem 5: Implement shut the box.
def isvalid(choices, numbers, roll):
    if sum(choices) != roll:
        return False

    for i in range(len(choices)):
        if numbers.count(choices[i]) == 0:
            return False

    return True

def end_score(name, numbers, initial_time, end):
    import time
    print("Game over!\n")
    print("Score for player " + name + ": " + str(sum(numbers)) + " points")
    print("Time played: " + str(round((time.time() - initial_time), 2)) + " seconds")
    end = True
    return end

def shut_the_box(name, my_time):
    import time
    import random
    import box

    initial_time = time.time()
    numbers = [1,2,3,4,5,6,7,8,9]
    die = [1,2,3,4,5,6]
    end = False

    while end == False:
        current_time = float(my_time) + (initial_time - time.time())
        current_time = round(current_time, 2)

        if current_time <= 0:
            end = end_score(name, numbers, initial_time, end)
            print("Better luck next time!")
            break

        if sum(numbers) <= 6:
            roll = sum(random.sample(die, 1))
        else:
            roll = sum(random.sample(die, 2))
            
        print("\nNumbers left: " + str(numbers))
        print("Roll: " + str(roll))

        if box.isvalid(roll, numbers):
            print("Seconds left: " + str(current_time))
            user_input = input("Numbers to eliminate: ")
            choices = box.parse_input(user_input, numbers)

            while isvalid(choices, numbers, roll) == False:
                current_time = float(my_time) + (initial_time - time.time())
                current_time = round(current_time, 2)
                print("Invalid input\n")
                print("Seconds left: " + str(current_time))
                user_input = input("Numbers to eliminate: ")
                choices = box.parse_input(user_input, numbers)

            for i in range(len(choices)):
                numbers.remove(choices[i])

        else:
            end = end_score(name, numbers, initial_time, end)
            print("Better luck next time!")

        if len(numbers) == 0:
            end = end_score(name, numbers, initial_time, end)
            print("Congratulations!! You shut the box!")




import sys
if len(sys.argv) == 3:
    shut_the_box(sys.argv[1], sys.argv[2])
