def print_iter(cls):
    class NewCls(cls):
        def __next__(self):
            line = super(NewCls, self).__next__()
            name = line[0]
            num_seq = line[1]
            result = open('./result.txt', 'w')
            result.writelines(name + ' ' + str(num_seq) + '\n')
            result.close()
            return line

    return NewCls


@print_iter
class GraphIter:
    def __init__(self, graph):
        self.graph = graph

        start_index = -1
        self.num = start_index
        self.sorted_graph = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.num + 1 >= len(self.graph):
            raise StopIteration
        else:
            self.num += 1
            return self.graph[self.num]

    def sorted(self):
        while len(self.graph) != 0:
            max_len_seq_item = 0
            max_len_seq = 0
            num_seq = 1
            counter = 0
            for i in self.graph:
                len_seq = i[num_seq]
                if len_seq > max_len_seq:
                    max_len_seq = len_seq
                    max_len_seq_item = counter
                counter += 1
            self.sorted_graph.append(self.graph.pop(max_len_seq_item))

        for _ in GraphIter(self.sorted_graph):
            pass
