def file_reader_generator(file):
    line = file.readline()
    if not line:
        return StopIteration
    line_split = line.split()
    seq_num = len(line_split) - 1
    seq = line_split[seq_num]
    if seq.count(seq[0]) == len(seq):
        yield line


class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file_obj = open(self.file_name, "r")
        self.file_obj.readline()  # read first line
        return file_reader_generator(self.file_obj)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
