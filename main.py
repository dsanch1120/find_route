# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import copy
from graph import Graph


def handleArgs():
    #    if len(sys.argv) != 4:
    #        sys.exit("Incorrect number of arguments")
    #    return [sys.argv[1], sys.argv[2], sys.argv[3]]
    return ["input1.txt", "yo", "yo"]  # FIXME


def createGraph(f_name, origin, destination):
    f = open(f_name, "r")
    f_lines = f.readlines()

    g = Graph()
    for i in f_lines:
        if i == '\n':
            continue
        s = copy.deepcopy(i.split())
        if s[0] == "END":
            break
        #g.add_node(s[0])
        g.add_path(s[0], s[1], s[2])

    print("Breakpoint")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = handleArgs()
    createGraph(args[0], args[1], args[2])
    print("Program ran successfully")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
