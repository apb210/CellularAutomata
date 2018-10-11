class SixValPattern():

    def __init__(self):
        self.pattern_map = dict()


    def addToMap(self, data):
        for line in data:
            if line[0] in self.pattern_map:
                self.pattern_map[line[0]].append(line[1])
            else:
                self.pattern_map[line[0]] = [line[1]]

    def printOccurrences(self, tuple):
        print (self.pattern_map[tuple])




