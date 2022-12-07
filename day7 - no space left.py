# Imports
from collections import defaultdict

# Read Puzzle input
with open("inputs/day7 - directory structure.txt", 'r') as file:
    lines = [i.strip() for i in file.readlines()[1:]]


# Class
class DirectoryTree:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        self.files = {}
        self.parent = parent

    def create_file(self, size, name):
        self.files[name] = int(size)

    def create_directory(self, name):
        return self.children.setdefault(name, DirectoryTree(name, parent=self))

    def __iter__(self):
        for child in self.children.values():
            yield child
            yield from child

    @property
    def root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root

    @property
    def size(self):
        return sum(self.files.values()) + sum(child.size for child in self.children.values())


# Main program
def main(part):
    cwd = DirectoryTree("/")
    for line in lines:
        match line.split():
            case ("$", "cd", dir_name):
                cwd = cwd.parent if dir_name == ".." else cwd.create_directory(dir_name)
            case ("dir", *_):
                continue
            case ("$", "ls"):
                continue
            case (size, name):
                cwd.create_file(size, name)
    print(lines)
    if part == "Part A":
        print(sum(children.size for children in cwd.root if children.size < 100000))
    if part == "Part B":
        print(min(children.size for children in cwd.root if 40000000 + children.size > cwd.root.size))


# Independent functions
if __name__ == "__main__":
    main("Part B")
