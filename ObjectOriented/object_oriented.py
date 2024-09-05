# object_oriented.py
"""Python Essentials: Object Oriented Programming.
Seong-Eun Cho
Math 321
September 19, 2017
"""


class Backpack:
    """A Backpack object class. Has a name and a list of contents.

    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
        color (str): the color of the backpack.
        max_size (int): the capacity of the contents.
    """

    # Problem 1: Modify __init__() and put(), and write dump().
    def __init__(self, name, color, max_size=5):
        """Set the name and initialize an empty list of contents.

        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the color of the backpack.
            max_size (int): the capacity of the contents. Default ot 5
        """
        self.name = name
        self.contents = []
        self.color = color
        self.max_size = max_size

    def put(self, item):
        """Add 'item' to the backpack's list of contents.
           If the number of contents exceeds the size capacity,
           print "No Room!" 
        """
        if len(self.contents) < self.max_size:
            self.contents.append(item)
        else:
            print("No Room!")

    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)

    def dump(self):
        """Resets the contents of the backpack"""
        self.contents = []

    # Magic Methods -----------------------------------------------------------

    # Problem 3: Write __eq__() and __str__().
    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color and len(self.contents) == len(other.contents)

    def __str__(self):
        s = "Owner:\t\t" + self.name + "\n"
        s += "Color:\t\t" + self.color + "\n"
        s += "Size:\t\t" + str(len(self.contents)) + "\n"
        s += "Max Size:\t" + str(self.max_size) + "\n"
        s += "Contents:\t" + str(self.contents)
        return s
# An example of inheritance. You are not required to modify this class.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size=3)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)

    def weight(self):
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum([len(str(item)) for item in self.contents])


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.
class Jetpack(Backpack):
    """A Jetpack object class. Inherits from the Backpack class.
    A jetpack is smaller than a backpack, and can fly using fuel.

    Attributes:
        name (str): the name of the jetpack's owner.
        color(str): the color of the jetpack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the jetpack.
        fuel (int): the amount of fuel left in the jetpack.
    """
    def __init__(self, name, color, max_size=2, fuel=10):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. Fuel is stored separately. A jetpack 
        only only 2 item by default.

        Parameters:
            name (str): the name of the jetpack's owner.
            color (str): the color of the jetpack.
            max_size(int): the maximum number of items that can fit inside.
            fuel (int): the amount of fuel left in the jetpack.
        """
        Backpack.__init__(self, name, color, max_size)
        self.fuel = fuel

    def fly(self, amount):
        """Spends a certain amount of fuel to fly. Prints Not enough Fuel!
        when the amount exceeds the fuel."""
        if amount > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel -= amount

    def dump(self):
        """Resets the contents of the jetpack and empies all fuel."""
        self.contents = []
        self.fuel = 0

# Problem 4: Write a 'ComplexNumber' class.
class ComplexNumber:

    def __init__(self, real, imag):

        self.real = real
        self.imag = imag

    def conjugate(self):
        conj = ComplexNumber(self.real, -self.imag)
        return conj

    def __str__(self):
        if self.imag >= 0:
            return "("+str(self.real)+"+"+str(self.imag)+"j)"
        else:
            return "("+str(self.real)+str(self.imag)+"j)"

    def __abs__(self):
        from math import sqrt
        return sqrt(self.real**2 + self.imag**2)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return ComplexNumber(r, i)

    def __truediv__(self, other):
        d = other.real**2 + other.imag**2
        r = (self.real*other.real + self.imag*other.imag)/d
        i = (self.imag*other.real - self.real*other.imag)/d
        return ComplexNumber(r, i)


# Test functions
def test_prob1():
    testpack = Backpack("Barry", "black") # Instantiate the object.
    if testpack.name != "Barry": # Test an attribute.
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer", "wallet"]:
        testpack.put(item) # Test a method.
    print("Name:", testpack.name)
    print("Color:", testpack.color)
    print("Contents:", testpack.contents)
    testpack.put("calculator")
    print("Contents:", testpack.contents)
    testpack.dump()
    print("Contents:", testpack.contents)

def test_prob2():
    testpack = Jetpack("Mann", "blue", max_size=4, fuel=15)
    testpack.put("grenade")
    print("Name:", testpack.name)
    print("Color:", testpack.color)
    print("Max size:", str(testpack.max_size))
    print("Fuel:", str(testpack.fuel))
    print("Contents:", str(testpack.contents))
    testpack.fly(10)
    print("Fuel after flying:", str(testpack.fuel))
    testpack.fly(10)
    testpack.dump()
    print("Fuel:", str(testpack.fuel))
    print("Contents:", str(testpack.contents))


def test_prob3():
    testpack1 = Backpack("Barry", "black")
    testpack2 = Backpack("Barry", "black")
    testpack3 = Backpack("Ken", "red")
    testpack3.put("pencil")

    print(str(testpack1 + testpack3)) #should return 1

    if testpack1 < testpack3: #should be true
        print("testpack1 < testpack3")
    else:
        print("testpack1 >= testpack3")

    if testpack1 == testpack2: #should be true
        print("testpack1 == testpack2")
    else:
        print("testpack1 != testpack2")

    if testpack1 == testpack3: #should be false
        print("testpack1 == testpack3")
    else:
        print("testpack1 != testpack3")

    print(testpack3)

def test_prob4(a, b):
    py_cnum, cnum = complex(a,b), ComplexNumber(a, b)
    py_cnum2, cnum2 = complex(a+1, b+3), ComplexNumber(a+1, b+3)
    conj = cnum.conjugate()
    print(cnum)
    print(conj)
    print(abs(cnum))
    print(cnum + cnum2)
    print(cnum - cnum2)
    print(cnum * cnum2)
    print(cnum / cnum2)

    # Validate the constructor.
    if cnum.real != a or cnum.imag != b:
        print("__init__() set self.real and self.imag incorrectly")
    # Validate conjugate() by checking the new number's imag attribute.
    if py_cnum.conjugate().imag != cnum.conjugate().imag:
        print("conjugate() failed for", py_cnum)
    # Validate __str__().
    if str(py_cnum) != str(cnum):
        print("__str__() failed for", py_cnum)
    # Validate __eq__().
    if py_cnum != cnum:
        print("__eq__() failed for", py_cnum)
    # Validate __add__().
    if py_cnum+py_cnum2 != cnum+cnum2:
        print("__add__() failed for", py_cnum)
    # Validate __sub__().
    if py_cnum-py_cnum2 != cnum-cnum2:
        print("__sub__() failed for", py_cnum)
    # Validate __mul__().
    if py_cnum*py_cnum2 != cnum*cnum2:
        print("__mul__() failed for", py_cnum)
    # Validate __truediv__().
    if py_cnum/py_cnum2 != cnum/cnum2:
        print("__truediv__() failed for", py_cnum)
