# exceptions_fileIO.py
"""Python Essentials: Exceptions and File Input/Output.
<Name>
<Class>
<Date>
"""

from random import choice


# Problem 1
def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                                           "digits differ by 2 or more: ")
    if not step_1.isdigit():
        raise ValueError("The first number (step_1) is not a 3-digit number.")
    else:
        if len(step_1) != 3:
            raise ValueError("The first number (step_1) is not a 3-digit number.")

    if abs(int(step_1[0]) - int(step_1[2])) < 2:
        raise ValueError("The first number’s first and last digits differ by less than 2.")

    step_2 = input("Enter the reverse of the first number, obtained "
                                              "by reading it backwards: ")
    if step_2[::-1] != step_1:
        raise ValueError("The second number (step_2) is not the reverse of the first number.")

    step_3 = input("Enter the positive difference of these numbers: ")
    if str(abs(int(step_1) - int(step_2))) != step_3:
        raise ValueError("The third number (step_3) is not the positive difference of the first two numbers.")

    step_4 = input("Enter the reverse of the previous result: ")
    if step_4[::-1] != step_3:
        raise ValueError("The fourth number (step_4) is not the reverse of the third number.")


    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")


# Problem 2
def random_walk(max_iters=1e12):
    iter = 0

    try:
        walk = 0
        directions = [1, -1]
        for i in range(int(max_iters)):
            walk += choice(directions)
            iter += 1

        print("Process completed")

    except KeyboardInterrupt as e:
        print("Process interrupted at iteration", iter)
    finally:
        return walk


# Problems 3 and 4: Write a 'ContentFilter' class.
class ContentFilter:

    def __init__(self, file_name):
        self.file_name = file_name
        self.contents = []
        self.ocontents = []
        self.open_file()
        self.clean_contents()
        self.char = 0
        self.alphachar = 0
        self.numchar = 0
        self.wschar = 0
        self.numlines = len(self.contents)
        self.count_characters()

    def open_file(self):
        try:
            with open(self.file_name, 'r') as myfile:
                self.ocontents = myfile.readlines()

        except (FileNotFoundError, TypeError, OSError) as e:
            self.file_name = input("Please enter a valid file name: ")
            self.open_file()

    def clean_contents(self):
        for i in range(len(self.ocontents)):
            nl = self.ocontents[i].find("\n")
            if nl != -1:
                self.contents.append(self.ocontents[i][:nl])
            else:
                self.contents.append(self.ocontents[i])

    def count_characters(self):
        for i in range(len(self.ocontents)):
            self.char += len(self.ocontents[i])
            for j in range(len(self.ocontents[i])):
                if self.ocontents[i][j].isalpha():
                    self.alphachar += 1
                elif self.ocontents[i][j].isdigit():
                    self.numchar += 1
                elif self.ocontents[i][j].isspace():
                    self.wschar += 1


    def uniform(self, outfile_name, mode='w', case="upper"):
        #handle exceptions for mode
        if mode != 'w' and mode != 'x' and mode != 'a':
            raise ValueError("Mode must be 'w', 'x', or 'a'!")
        #handle exceptions for case
        elif case != "upper" and case != "lower":
            raise ValueError("Case must be \"upper\" or \"lower\"!")
        #if the values are correct, run the method
        else:
            with open(outfile_name, mode) as outfile:
                if case == "upper":
                    for i in range(len(self.contents)):
                        outfile.write(self.contents[i].upper()+'\n')
                else:
                    for i in range(len(self.contents)):
                        outfile.write(self.contents[i].lower()+'\n')

    def reverse(self, outfile_name, mode='w', unit="line"):
        #handle exceptions for mode
        if mode != 'w' and mode != 'x' and mode != 'a':
            raise ValueError("Mode must be 'w', 'x', or 'a'!")
        #handle exceptions for unit
        elif unit != "line" and unit != "word":
            raise ValueError("Unit must be \"line\" or \"word\"!")
        else:
            with open(outfile_name, mode) as outfile:
                if unit == "line":
                    for i in range(len(self.contents)-1, -1, -1):
                        outfile.write(self.contents[i]+'\n')
                else:
                    for i in range(len(self.contents)):
                        outfile.write(self.contents[i][::-1]+'\n')

    def transpose(self, outfile_name, mode='w'):
        import numpy as np
        #handle exceptions for mode
        if mode != 'w' and mode != 'x' and mode != 'a':
            raise ValueError("Mode must be 'w', 'x', or 'a'!")
        elif len(self.contents) != 0:
            tr = []
            for i in range(len(self.contents)):
                tr.append(self.contents[i].split())

            tr = np.array(tr)
            tr = tr.T

            with open(outfile_name, mode) as outfile:
                for i in range(len(tr)):
                    for j in range(len(tr[i])):
                        if j != len(tr[i])-1:
                            outfile.write(tr[i][j]+' ')
                        else:
                            outfile.write(tr[i][j]+'\n')

    def __str__(self):
        s = "SourceFile:\t\t" + self.file_name + '\n'
        s += "Total characters:\t" + str(self.char) + '\n'
        s += "Alphabetic characters:\t" + str(self.alphachar) + '\n'
        s += "Numerical characters:\t" + str(self.numchar) + '\n'
        s += "Whitespace characters:\t" + str(self.wschar) + '\n'
        s += "Number of lines:\t" + str(self.numlines)
        return s
