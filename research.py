# The format of the data
# ID	Name	Hour(hour)	Machine	Seq
# Pavel Seredentsev	Arkadiy Verdiev	Arkadiy Verdiev	Svetlana Lupashova	CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

class Research:
    def __init__(self, line):
        line = line.split()
        self.seq = line[len(line) - 1]

        self.names = []
        len_mas = (len(line) - 2) // 2
        for i in range(len_mas):
            name = line[2 * i] + ' ' + line[2 * i + 1]
            self.names.append(name)
