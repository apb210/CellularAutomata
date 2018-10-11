"""
    This code implements Rule 30 of Stephen Wolfram's Cellular Automata examples.

    The code expects a first_row.csv file containing the initial condition and the number of steps to evolve.

    It prints out the entire matrix as well as occurrences of three patterns:
        (1-1-0/1-0-0, 1-1-0/1-0-1, 1-1-0,1-1-0)

    It should be noted that the last pattern is not expected to be observed since as per rule 30,
    (1,1,0) is always 0 so as per this rule the central element in the subsequent row should always be zero.



    Run this program by:

        python main.py first_row.csv 100

        for 100 steps of evolution.


    ****
    This program uses the very basic features of the python interpreter. No libraries have been used not even
    the basic ones as numpy.
    ****
"""


import sys


class Rule30():
    """
    This is the Rule 30 class. It contains the rules and the method to
    generate a new row.
    """


    def __init__(self, cols):
        self._cols = cols



    def Rule30_rules(self, _tple_of_3):
        return {
            (1, 1, 1): 0,
            (1, 1, 0): 0,
            (1, 0, 1): 0,
            (1, 0, 0): 1,
            (0, 1, 1): 1,
            (0, 1, 0): 1,
            (0, 0, 1): 1,
            (0, 0, 0): 0,

        }[_tple_of_3]


    def generate_new_row(self, prev_row, pattern_map_instance, j):

        _new_row = []
        _new_row.append(0)


        #Fill using Rule 30
        for i in range(1, self._cols - 1):
            _tuple = (prev_row[i-1], prev_row[i], prev_row[i + 1])
            _new_row.append(self.Rule30_rules(_tuple))


        #Using Periodic Boundary Conditions
        _new_row.append(_new_row[1])
        _new_row[0] = _new_row[self._cols - 2]


        _pattern_list = []

        for i in range(1, self._cols - 1):
            _pattern = (prev_row[i-1], prev_row[i], prev_row[i+1],
                        _new_row[i-1], _new_row[i], _new_row[i+1])
            _pattern_list.append((_pattern, (i, j)))
        pattern_map_instance.addToMap(_pattern_list)
        return _new_row, _pattern_list





class SixValPattern():
    """
    This class contains the methods to organize the pattern map.
    A dictionary is implemented where the flattened Six Value Pattern
    is organized as a tuple and used as a key which can be queried to
    for the coordinates in the form of (x_i, y_j) representing x_i column and y_j row.


    """

    def __init__(self):
        self.pattern_map = dict()


    def addToMap(self, data):
        for line in data:
            if line[0] in self.pattern_map:
                self.pattern_map[line[0]].append(line[1])
            else:
                self.pattern_map[line[0]] = [line[1]]

    def get_pattern_occurrences(self, tuple):
        print (self.pattern_map[tuple])





def main():


    def new_row(instance_Rule_30, prev_row, pattern_map, j):
        Row_from_rule30 = instance_Rule_30.generate_new_row(prev_row, pattern_map, j)
        return Row_from_rule30



    #Read File from command line
    inputfile = open(sys.argv[1], 'r')

    first_row = [row.strip('\n').split(',') for row in inputfile]
    NCols = len(first_row[0])

    prev_row = [int(first_row[0][i]) for i in range(len(first_row[0]))]
    NRows = int(sys.argv[2])

    #Initialize Matrix
    matrix = []

    matrix.append(prev_row)

    #Instantiate the Rule 30 and the pattern map objects
    instance_of_rule30 = Rule30(NCols)
    pattern_map_instance = SixValPattern()


    # Evolve
    for j in range(1, NRows):
        next_row, pattern_list = new_row(instance_of_rule30, prev_row, pattern_map_instance, j)
        matrix.append(next_row)
        prev_row = next_row

    #Print the Matrix
    for row in matrix:
        print (" ")
        for each in row:
            print (each, end = ' ')

    print (" ")



    #Pattern occurrences Please note that the matrix is flattened

    try:
        print("\n","Pattern Occurrence of 1-1-0/1-0-0", "\n")
        pattern_map_instance.get_pattern_occurrences((1, 1, 0, 1, 0, 0))
    except KeyError:
        print("Not found")

    try:
        print("\n","Pattern Occurrence of 1-1-0/1-0-1","\n")
        pattern_map_instance.get_pattern_occurrences((1, 1, 0, 1, 0, 1))
    except KeyError:
        print("Not found")

    try:
        print("\n","Pattern Occurrence of 1-1-0/1-1-0","\n")
        pattern_map_instance.get_pattern_occurrences((1, 1, 0, 1, 1, 0))
    except KeyError:
        print("Not found")




if __name__ == "__main__":

    Usage = """
    
        Usage:
            main.py first_row.csv NRows

        Where:
            first_row.csv contains the first row as initial condition
            NRows specifies the number of steps to evolve

    """
    if len(sys.argv) < 3:
        print(Usage)
        sys.exit(0)

    main()