#                                                  FILE MANAGER
class FileManageer:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None  # referinta fisierului deschis

    def __enter__(self):
        self.file = open(self.filename, self.mode)  # deschidem fisierul si stocam referinta
        return self.file  # permite utilizarea lui "as f" in blocul "with"

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close


with FileManageer('data.txt', 'w') as f:  # cu ajutorul clasei dechidem fisierul cu modul write
    f.write('Text')

from contextlib import contextmanager


@contextmanager
def fileManager(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


with fileManager('data2.txt', 'w') as f:
    f.write('Text 2 ')
