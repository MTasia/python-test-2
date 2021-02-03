import os
from os import listdir
from os.path import isfile, isdir, join, splitext


def print_iter(cls):
    class NewCls(cls):
        def __next__(self):
            x = super(NewCls, self).__next__()
            if isfile(x) and splitext(x)[1] == '.txt':
                print(x)
            return x
    return NewCls


@print_iter
class DirReader:
    def __init__(self, path):
        self.path = path
        self.contain = []
        for i in listdir(path):
            self.contain.append(join(path, i))
        start_index = -1
        self.num = start_index
        self.list_file = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.num + 1 >= len(self.contain):
            raise StopIteration
        else:
            self.num += 1
            return self.contain[self.num]

    def find_file(self, to_visit):
        if len(to_visit) == 0:
            return self.list_file
        else:
            current_direc = to_visit.pop()
            for direc in DirReader(current_direc):
                if isfile(direc) and splitext(direc)[1] == '.txt':
                    self.list_file.append(direc)
                elif isdir(direc):
                    to_visit.append(direc)
                    self.find_file(to_visit)
            return self.list_file


# def find_file(to_visit, list_file):
#     if len(to_visit) == 0:
#         return list_file
#     else:
#         current_direc = to_visit.pop()
#         current_direc_contain = listdir(current_direc)
#         for direc in DirReader(current_direc):
#             if isfile(direc):
#                 list_file.append(direc)
#             elif isdir(direc):
#                 to_visit.append(direc)
#                 find_file(to_visit, list_file)
