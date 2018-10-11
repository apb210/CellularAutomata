class Rule30():

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
        #Generate pattern Map
        for i in range(1, self._cols - 1):
            _pattern = (prev_row[i-1], prev_row[i], prev_row[i+1],
                        _new_row[i-1], _new_row[i], _new_row[i+1])
            _index = i

            _pattern_list.append((_pattern, (j,i)))

            #print ("Pattern :",_pattern)

        #print (_pattern_list)
        pattern_map_instance.addToMap(_pattern_list)

        return _new_row, _pattern_list







