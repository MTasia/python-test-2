import os
from src import dir_reader
from src import file_reader
from src import research
from src import graph_iter


def reading_file(list_file):
    to_research = []
    for file in list_file:
        with file_reader.FileReader(file) as record_reader:
            for record in record_reader:
                to_research.append(record)
    return to_research


def create_graph(researches):
    # create graph
    graph = {}
    for i in range(len(researches)):
        current_research = research.Research(researches[i])
        current_names = current_research.names
        current_seq = current_research.seq
        if len(current_names) > 1:
            for name in current_names:
                if name in graph:
                    graph[name].append(current_seq)
                else:
                    graph[name] = [current_seq]
    return graph


def graph_to_list(graph):
    graph_list = []
    for i in graph:
        pair = [i, len(graph[i])]
        graph_list.append(pair)
    return graph_list


def main():
    path = 'data'
    to_visit = [path]

    # get needed file from data (file with extension .txt)
    list_file = dir_reader.DirReader(path).find_file(to_visit)

    # get needed string from file for researches
    researches = reading_file(list_file)

    # create graph
    graph = create_graph(researches)

    # write sorted graph in result.txt
    graph = graph_to_list(graph)
    graph_iter.GraphIter(graph).sorted()


if __name__ == '__main__':
    main()
